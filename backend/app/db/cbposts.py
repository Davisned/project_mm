import uuid

from sqlmodel import Session, select

from app.models.cbpost import (
    CBPostCreate,
    CBPostUpdate,
    CBPost,
)


def create_cbpost(session: Session, cbpost_in: CBPostCreate) -> CBPost:
    """
    Create a new CBPost in the database.
    """
    db_obj = CBPost.model_validate(cbpost_in)

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_cbpost(session: Session, cbpost_id: uuid.UUID) -> CBPost | None:
    """
    Get a CBPost by ID.
    """
    statement = select(CBPost).where(CBPost.id == cbpost_id)
    return session.exec(statement).first()


def update_cbpost(session: Session, id: uuid.UUID, cbpost_in: CBPostUpdate) -> CBPost:
    """
    Update a CBPost in the database.
    """
    db_obj = get_cbpost(session, id)
    if not db_obj:
        raise ValueError(f"CBPost with id {id} not found")

    new_data = cbpost_in.model_dump(exclude_unset=True)

    for key, value in new_data.items():
        setattr(db_obj, key, value)

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def delete_cbpost(session: Session, cbpost_id: uuid.UUID) -> CBPost:
    """
    Delete a CBPost by ID.
    """
    db_obj = get_cbpost(session, cbpost_id)
    if not db_obj:
        raise ValueError(f"CBPost with id {cbpost_id} not found")

    session.delete(db_obj)
    session.commit()
    return db_obj


def get_all_cbposts(session: Session) -> list[CBPost]:
    """
    Get all CBPosts.
    """
    statement = select(CBPost)
    return session.exec(statement).all()
