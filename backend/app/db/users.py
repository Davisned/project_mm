import uuid

from sqlmodel import Session, select

from app.models.user import (
    UserCreate,
    UserUpdate,
    User,
)
from app.security import get_password_hash, verify_password


def create_user(session: Session, user_in: UserCreate) -> User:
    """
    Create a new user in the database
    """
    db_obj = User.model_validate(
        user_in,
        update={"hashed_password": get_password_hash(user_in.password)},
    )

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user(session: Session, user_id: uuid.UUID) -> User | None:
    """
    Get a user by ID
    """
    statement = select(User).where(User.id == user_id)
    return session.exec(statement).first()


def get_user_by_email(session: Session, email: str) -> User | None:
    """
    Get a user by email
    """
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


def update_user(session: Session, id: uuid.UUID, user_in: UserUpdate) -> User:
    """
    Update a user in the database
    """
    db_obj = get_user(session, id)
    if not db_obj:
        raise ValueError(f"User with id {id} not found")

    new_data = user_in.model_dump(exclude_unset=True)
    extra_data = {}
    if password := new_data.pop("password", None):
        extra_data["hashed_password"] = get_password_hash(password)

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def delete_user(session: Session, id: uuid.UUID) -> User:
    """
    Delete a user from the database
    """
    db_obj = get_user(session, id)
    if not db_obj:
        raise ValueError(f"User with id {id} not found")

    session.delete(db_obj)
    session.commit()
    return db_obj


def authenticate_user(session: Session, email: str, password: str) -> User | None:
    """
    Authenticate a user by email and password
    """
    user = get_user_by_email(session, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def get_all_users(session: Session) -> list[User]:
    """
    Get all users from the database
    """
    statement = select(User)
    return list(session.exec(statement).all())
