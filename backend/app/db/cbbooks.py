import uuid

from sqlmodel import Session, select
from app.models.cbbook import (
    CBBookCreate,
    CBBookUpdate,
    CBBook,
)


def create_cbbook(session: Session, cbbook_in: CBBookCreate) -> CBBook:
    """
    Create a new CBBook in the database
    """
    db_obj = CBBook.model_validate(cbbook_in)

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_cbbook(session: Session, cbbook_id: uuid.UUID) -> CBBook | None:
    """
    Get a CBBook by ID
    """
    statement = select(CBBook).where(CBBook.id == cbbook_id)
    return session.exec(statement).first()


def update_cbbook(session: Session, id: uuid.UUID, cbbook_in: CBBookUpdate) -> CBBook:
    """
    Update a CBBook in the database
    """
    db_obj = get_cbbook(session, id)
    if not db_obj:
        raise ValueError(f"CBBook with id {id} not found")

    new_data = cbbook_in.model_dump(exclude_unset=True)

    for key, value in new_data.items():
        setattr(db_obj, key, value)

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def delete_cbbook(session: Session, cbbook_id: uuid.UUID) -> CBBook:
    """
    Delete a CBBook from the database
    """
    db_obj = get_cbbook(session, cbbook_id)
    if not db_obj:
        raise ValueError(f"CBBook with id {cbbook_id} not found")

    session.delete(db_obj)
    session.commit()
    return db_obj


def get_all_cbbooks(session: Session) -> list[CBBook]:
    """
    Get all CBBooks from the database
    """
    statement = select(CBBook)
    return list(session.exec(statement).all())
