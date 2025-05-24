import uuid

from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cbpost import CBPost  # noqa: F401, pylint: disable=unused-import
    from .user import User  # noqa: F401, pylint: disable=unused-import


class CBBookBase(SQLModel):
    """Base model for CBBook."""

    first_name: str
    last_name: str
    middle_name: str | None = None
    title: str | None = None
    maiden_name: str | None = None
    date_of_birth: datetime | None = None
    date_of_death: datetime | None = None


class CBBookCreate(CBBookBase):
    """Model for creating a new CBBook."""

    owner_id: uuid.UUID = Field(nullable=False)


class CBBookUpdate(CBBookBase):
    """Model for updating an existing CBBook."""

    pass


class CBBook(CBBookBase, table=True):
    """Model for CBBook."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, index=True)
    deleted_at: datetime | None = None

    posts: list["CBPost"] = Relationship(
        back_populates="cbbook",
    )

    owner_id: uuid.UUID = Field(
        foreign_key="user.id",
        index=True,
    )
    owner: "User" = Relationship(
        back_populates="cbbooks",
        sa_relationship_kwargs={"lazy": "joined"},
    )


class CBBookRead(CBBookBase):
    """Model for reading a CBBook."""

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
