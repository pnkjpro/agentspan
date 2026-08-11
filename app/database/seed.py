from app.database.connection import SessionLocal
from app.database.models import User


users = [
    {
        "user_id": "USR-10001",
        "name": "Rahul Sharma",
        "email": "rahul.sharma@example.com",
    },
    {
        "user_id": "USR-10002",
        "name": "Priya Verma",
        "email": "priya.verma@example.com",
    },
    {
        "user_id": "USR-10003",
        "name": "Amit Kumar",
        "email": "amit.kumar@example.com",
    },
    {
        "user_id": "USR-10004",
        "name": "Neha Singh",
        "email": "neha.singh@example.com",
    },
    {
        "user_id": "USR-10005",
        "name": "Vikas Gupta",
        "email": "vikas.gupta@example.com",
    },
    {
        "user_id": "USR-10006",
        "name": "Anjali Mehta",
        "email": "anjali.mehta@example.com",
    },
    {
        "user_id": "USR-10007",
        "name": "Rohit Agarwal",
        "email": "rohit.agarwal@example.com",
    },
    {
        "user_id": "USR-10008",
        "name": "Sneha Kapoor",
        "email": "sneha.kapoor@example.com",
    },
]


def seed_users():
    db = SessionLocal()

    try:
        for user_data in users:
            existing_user = (
                db.query(User)
                .filter(User.user_id == user_data["user_id"])
                .first()
            )

            if existing_user:
                continue

            db.add(User(**user_data))

        db.commit()

        print(f"Seeded {len(users)} mock users.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_users()