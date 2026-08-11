from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.services.user_service import get_user


def get_user_by_id(user_id: str) -> dict:
    """
    Look up a user by user_id in the MySQL users table.
    """
    db: Session = SessionLocal()

    try:
        user = get_user(db, user_id)

        if not user:
            return {
                "found": False,
                "user_id": user_id,
            }

        return {
            "found": True,
            "user": {
                "user_id": user.user_id,
                "name": user.name,
                "email": user.email,
            },
        }

    finally:
        db.close()