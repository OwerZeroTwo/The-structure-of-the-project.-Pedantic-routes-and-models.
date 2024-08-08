from fastapi import APIRouter

router = APIRouter()

from .task import router as task_router
from .user import router as user_router

router.include_router(task_router)
router.include_router(user_router)