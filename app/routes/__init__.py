from fastapi import APIRouter

from .health import router as health_router
from .sse import router as sse_router
from .users import router as users_router
from .auth import router as auth_router

api_router = APIRouter()

# 应用健康接口
api_router.include_router(health_router)

# 应用 sse 测试接口
api_router.include_router(sse_router)

api_router.include_router(auth_router)

api_router.include_router(users_router)




