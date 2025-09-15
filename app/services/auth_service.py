from sqlmodel import Session, select

from app.models import User, UserCreate
from app.core import verify_password
from .base_service import BaseService


def get_user_by_email(*, session: Session, email: str) -> User | None:
    """
    get user by email
    :param session:
    :param email:
    :return:
    """
    session_user = session.exec(
        select(User).where(User.email == email)
    ).first()
    return session_user


def auth_by_email(*, session: Session, email: str, password: str) -> User | None:
    """
    authenticate user with email and password
    :param session:
    :param email:
    :param password:
    :return:
    """
    db_user = get_user_by_email(session=session, email=email)
    if db_user is None:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user


class AuthService(BaseService):
    pass