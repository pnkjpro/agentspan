from app.services.exception_service import (
    get_exception_logs,
    get_exception_by_file,
)


def find_user_exceptions(user_id: str) -> dict:
    """
    Find all exception logs associated with a specific user.
    """
    exceptions = get_exception_logs()

    matches = [
        exception
        for exception in exceptions
        if exception["user_id"] == user_id
    ]

    return {
        "user_id": user_id,
        "count": len(matches),
        "exceptions": [
            {
                "file": exception["file"],
                "request_id": exception["request_id"],
                "exception": exception["exception"],
                "service": exception["service"],
                "severity": exception["severity"],
            }
            for exception in matches
        ],
    }


def read_exception_log(filename: str) -> dict:
    """
    Read the complete contents of a specific exception log.
    """
    exception = get_exception_by_file(filename)

    if not exception:
        return {
            "found": False,
            "filename": filename,
        }

    return {
        "found": True,
        **exception,
    }