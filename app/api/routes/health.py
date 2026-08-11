from fastapi import APIRouter

from app.database.connection import test_connection


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/db")
def database_health():
    try:
        test_connection()

        return {
            "status": "ok",
            "database": "connected",
        }

    except Exception as exc:
        return {
            "status": "error",
            "database": "disconnected",
            "error": str(exc),
        }