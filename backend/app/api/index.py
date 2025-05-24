from fastapi import APIRouter

from .routes import login, users, cbbooks, cbposts

router = APIRouter()
# Include the routers from different modules
router.include_router(login.router, tags=["login"])
router.include_router(users.router, tags=["users"])
router.include_router(cbbooks.router, tags=["cbbooks"])
router.include_router(cbposts.router, tags=["cbposts"])
# Add more routers as needed
