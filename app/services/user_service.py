from sqlalchemy.orm import Session

from app.database.models import User


def get_user(db: Session, user_id: str) -> User | None:
    return (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )