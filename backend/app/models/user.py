import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cbpost import CBPost  # noqa: F401, pylint: disable=unused-import
    from .cbbook import CBBook  # noqa: F401, pylint: disable=unused-import


class UserBase(SQLModel):
    """Base model for User."""

    email: EmailStr = Field(nullable=False, unique=True, index=True)
    display_name: str | None = None


class UserCreate(UserBase):
    """Model for creating a new User."""

    password: str = Field(nullable=False, min_length=8)


class UserUpdate(UserBase):
    """Model for updating an existing User."""

    password: str = Field(nullable=False, min_length=8)


class User(UserBase, table=True):
    """Model for User."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str = Field(nullable=False)

    cbbooks: list["CBBook"] = Relationship(back_populates="owner")
    posts: list["CBPost"] = Relationship(back_populates="creator")


class UserRead(UserBase):
    """Model for reading a User."""

    id: uuid.UUID
