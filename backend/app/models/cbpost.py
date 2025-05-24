import uuid

from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

from .cbbook import CBBook
from .user import User


class CBPostBase(SQLModel):
    """Base model for CBPost."""

    title: str | None = None
    content_blob: bytes
    content_type: str
    content_size: int


class CBPostCreate(CBPostBase):
    """Model for creating a new CBPost."""

    cbbook_id: uuid.UUID = Field(nullable=False)

    creator_id: uuid.UUID | None = Field(default=None)


class CBPostUpdate(CBPostBase):
    """Model for updating an existing CBPost."""

    pass


class CBPost(CBPostBase, table=True):
    """Model for CBPost."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, index=True)
    deleted_at: datetime | None = None

    cbbook_id: uuid.UUID = Field(nullable=False, foreign_key="cbbook.id", index=True)
    cbbook: "CBBook" = Relationship(back_populates="posts", sa_relationship_kwargs={"lazy": "joined"})

    creator_id: uuid.UUID | None = Field(
        default=None,
        foreign_key="user.id",
        index=True,
    )
    creator: User | None = Relationship(back_populates="posts", sa_relationship_kwargs={"lazy": "joined"})


class CBPostRead(CBPostBase):
    """Model for reading a CBPost."""

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
