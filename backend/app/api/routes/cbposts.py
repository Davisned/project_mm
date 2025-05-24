import uuid

from fastapi import APIRouter, HTTPException, status

from app.db import cbposts as cbposts_db
from app.models.cbpost import CBPostCreate, CBPostRead, CBPostUpdate

from ..dependencies import Db_Session_Dep


router = APIRouter(prefix="/cbposts", tags=["cbposts"])


@router.post(
    "/",
    response_model=CBPostRead,
    status_code=status.HTTP_201_CREATED,
    operation_id="create_cbpost",
)
def create_cbpost(cbpost_in: CBPostCreate, session: Db_Session_Dep) -> CBPostRead:
    """
    Create a new CBPost.
    """
    cbpost = cbposts_db.create_cbpost(session, cbpost_in)
    if not cbpost:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CBPost already exists",
        )
    return cbpost


@router.get(
    "/{cbpost_id}",
    response_model=CBPostRead,
    status_code=status.HTTP_200_OK,
    operation_id="get_cbpost_by_id",
)
def get_cbpost_by_id(
    cbpost_id: uuid.UUID,
    session: Db_Session_Dep,
) -> CBPostRead:
    """
    Get a CBPost by ID.
    """
    cbpost = cbposts_db.get_cbpost(session, cbpost_id)
    if not cbpost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CBPost not found",
        )
    return cbpost


@router.put(
    "/{cbpost_id}",
    response_model=CBPostRead,
    status_code=status.HTTP_200_OK,
    operation_id="update_cbpost",
)
def update_cbpost(
    cbpost_id: uuid.UUID,
    cbpost_in: CBPostUpdate,
    session: Db_Session_Dep,
) -> CBPostRead:
    """
    Update a CBPost.
    """
    cbpost = cbposts_db.update_cbpost(session, cbpost_id, cbpost_in)
    if not cbpost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CBPost not found",
        )
    return cbpost


@router.delete(
    "/{cbpost_id}",
    response_model=CBPostRead,
    status_code=status.HTTP_200_OK,
    operation_id="delete_cbpost",
)
def delete_cbpost(
    cbpost_id: uuid.UUID,
    session: Db_Session_Dep,
) -> CBPostRead:
    """
    Delete a CBPost by ID.
    """
    cbpost = cbposts_db.delete_cbpost(session, cbpost_id)
    if not cbpost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CBPost not found",
        )
    return cbpost


@router.get(
    "/",
    response_model=list[CBPostRead],
    status_code=status.HTTP_200_OK,
    operation_id="get_all_cbposts",
)
def get_all_cbposts(
    session: Db_Session_Dep,
) -> list[CBPostRead]:
    """
    Get all CBPosts.
    """
    cbposts = cbposts_db.get_all_cbposts(session)
    if not cbposts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No CBPosts found",
        )
    return cbposts
