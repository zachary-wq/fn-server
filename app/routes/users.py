from fastapi import APIRouter

from .deps import CurrentUser
from app.models import UserPublic

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserPublic)
def get_me(current_user: CurrentUser) -> UserPublic:
    """
    get current user.
    :param current_user:
    :return:
    """
    return current_user

