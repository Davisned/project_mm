import uuid

from fastapi import APIRouter, HTTPException, status

from app.db import cbbooks as cbbooks_db
from app.models.cbbook import CBBookCreate, CBBookRead, CBBookUpdate

from ..dependencies import Db_Session_Dep


router = APIRouter(prefix="/cbbooks", tags=["cbbooks"])


@router.post(
    "/",
    response_model=CBBookRead,
    status_code=status.HTTP_201_CREATED,
    operation_id="create_cbbook",
)
def create_cbbook(cbbook_in: CBBookCreate, session: Db_Session_Dep) -> CBBookRead:
    """
    Create a new CBBook.
    """
    cbbook = cbbooks_db.create_cbbook(session, cbbook_in)
    if not cbbook:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CBBook already exists",
        )
    return cbbook


@router.get(
    "/{cbbook_id}",
    response_model=CBBookRead,
    status_code=status.HTTP_200_OK,
    operation_id="get_cbbook_by_id",
)
def get_cbbook_by_id(
    cbbook_id: uuid.UUID,
    session: Db_Session_Dep,
) -> CBBookRead:
    """
    Get a CBBook by ID.
    """
    cbbook = cbbooks_db.get_cbbook(session, cbbook_id)
    if not cbbook:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CBBook not found",
        )
    return cbbook


@router.put(
    "/{cbbook_id}",
    response_model=CBBookRead,
    status_code=status.HTTP_200_OK,
    operation_id="update_cbbook",
)
def update_cbbook(
    cbbook_id: uuid.UUID,
    cbbook_in: CBBookUpdate,
    session: Db_Session_Dep,
) -> CBBookRead:
    """
    Update a CBBook.
    """
    cbbook = cbbooks_db.update_cbbook(session, cbbook_id, cbbook_in)
    if not cbbook:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CBBook not found",
        )
    return cbbook


@router.delete(
    "/{cbbook_id}",
    response_model=CBBookRead,
    status_code=status.HTTP_200_OK,
    operation_id="delete_cbbook",
)
def delete_cbbook(
    cbbook_id: uuid.UUID,
    session: Db_Session_Dep,
) -> CBBookRead:
    """
    Delete a CBBook.
    """
    cbbook = cbbooks_db.delete_cbbook(session, cbbook_id)
    if not cbbook:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CBBook not found",
        )
    return cbbook


@router.get(
    "/",
    response_model=list[CBBookRead],
    status_code=status.HTTP_200_OK,
    operation_id="get_all_cbbooks",
)
def get_all_cbbooks(
    session: Db_Session_Dep,
) -> list[CBBookRead]:
    """
    Get all CBBooks.
    """
    cbbooks = cbbooks_db.get_all_cbbooks(session)
    return cbbooks
