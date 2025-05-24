import uuid

from fastapi import APIRouter, HTTPException, status

from app.db import users as users_db
from app.models.user import UserCreate, UserRead, UserUpdate

from ..dependencies import Db_Session_Dep


router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    operation_id="create_user",
)
def create_user(user_in: UserCreate, session: Db_Session_Dep) -> UserRead:
    """
    Create a new user.
    """
    user = users_db.create_user(session, user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    return user


@router.get(
    "/{user_id}",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
    operation_id="get_user_by_id",
)
def get_user_by_id(
    user_id: uuid.UUID,
    session: Db_Session_Dep,
) -> UserRead:
    """
    Get a user by ID.
    """
    user = users_db.get_user(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.put(
    "/{user_id}",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
    operation_id="update_user",
)
def update_user(
    user_id: uuid.UUID,
    user_in: UserUpdate,
    session: Db_Session_Dep,
) -> UserRead:
    """
    Update a user.
    """
    user = users_db.update_user(session, user_id, user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    operation_id="delete_user",
)
def delete_user(
    user_id: uuid.UUID,
    session: Db_Session_Dep,
) -> None:
    """
    Delete a user.
    """
    user = users_db.delete_user(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return None


@router.get(
    "/",
    response_model=list[UserRead],
    status_code=status.HTTP_200_OK,
    operation_id="get_users",
)
def get_users(
    session: Db_Session_Dep,
) -> list[UserRead]:
    """
    Get all users.
    """
    users = users_db.get_all_users(session)
    return users
