from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.user_service import get_user
from app.services.exception_service import get_exception_logs


router = APIRouter(
    prefix="/investigation",
    tags=["Investigation"],
)


@router.get("/{user_id}")
def investigate_user(
    user_id: str,
    db: Session = Depends(get_db),
):
    user = get_user(db, user_id)

    if not user:
        return {
            "user_found": False,
            "user_id": user_id,
            "exceptions": [],
        }

    all_exceptions = get_exception_logs()

    user_exceptions = [
        exception
        for exception in all_exceptions
        if exception["user_id"] == user_id
    ]

    return {
        "user_found": True,
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
        },
        "exception_count": len(user_exceptions),
        "exceptions": user_exceptions,
    }