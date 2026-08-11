from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.users import router as users_router
from app.api.routes.exceptions import router as exceptions_router
from app.api.routes.investigation import router as investigation_router


app = FastAPI(
    title="AgentSpan Investigation Service",
    version="1.0.0",
)


app.include_router(health_router)
app.include_router(health_router)
app.include_router(users_router)
app.include_router(exceptions_router)
app.include_router(investigation_router)


@app.get("/health")
def health():
    return {
        "status": "ok",
    }