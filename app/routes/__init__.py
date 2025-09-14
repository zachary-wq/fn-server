from fastapi import APIRouter

from .health import router as health_router
from .sse import router as sse_router

api_router = APIRouter()

# 应用健康接口
api_router.include_router(health_router)

# 应用 sse 测试接口
api_router.include_router(sse_router)




