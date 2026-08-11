from fastapi import APIRouter, HTTPException

from app.services.exception_service import (
    get_exception_logs,
    get_exception_by_file,
)


router = APIRouter(
    prefix="/exceptions",
    tags=["Exceptions"],
)


@router.get("")
def list_exceptions():
    return {
        "count": len(get_exception_logs()),
        "exceptions": get_exception_logs(),
    }


@router.get("/{filename}")
def get_exception(filename: str):
    exception = get_exception_by_file(filename)

    if not exception:
        raise HTTPException(
            status_code=404,
            detail="Exception log not found",
        )

    return exception