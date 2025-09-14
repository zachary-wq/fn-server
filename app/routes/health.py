from fastapi import APIRouter
from starlette.responses import PlainTextResponse

router = APIRouter(
    tags=["health"],
    prefix="/health",
)

@router.get("/home", response_class=PlainTextResponse)
def health_index():
    return "success"