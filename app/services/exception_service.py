from pathlib import Path
import re


EXCEPTION_DIR = Path("/var/www/code/exceptions")


def get_exception_logs() -> list[dict]:
    results = []

    if not EXCEPTION_DIR.exists():
        return results

    for file_path in sorted(EXCEPTION_DIR.glob("*.log")):
        content = file_path.read_text()

        user_match = re.search(r"user_id=(\S+)", content)
        request_match = re.search(r"request_id=(\S+)", content)
        exception_match = re.search(r"exception=(\S+)", content)
        service_match = re.search(r"service=(\S+)", content)
        severity_match = re.search(r"severity=(\S+)", content)

        results.append({
            "file": file_path.name,
            "user_id": user_match.group(1) if user_match else None,
            "request_id": request_match.group(1) if request_match else None,
            "exception": (
                exception_match.group(1)
                if exception_match else None
            ),
            "service": (
                service_match.group(1)
                if service_match else None
            ),
            "severity": (
                severity_match.group(1)
                if severity_match else None
            ),
            "raw_log": content,
        })

    return results


def get_exception_by_file(filename: str) -> dict | None:
    file_path = EXCEPTION_DIR / filename

    if not file_path.exists() or file_path.suffix != ".log":
        return None

    content = file_path.read_text()

    user_match = re.search(r"user_id=(\S+)", content)
    exception_match = re.search(r"exception=(\S+)", content)

    return {
        "file": filename,
        "user_id": user_match.group(1) if user_match else None,
        "exception": (
            exception_match.group(1)
            if exception_match else None
        ),
        "raw_log": content,
    }