from contextlib import asynccontextmanager
from fastapi import FastAPI

from fastapi_mcp import FastApiMCP
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.db.database import init_db
from app.api.dependencies import get_db_session
from app.api.index import router as main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for the FastAPI application.
    Mainly used to initialize the database for the first time.
    """
    db = next(get_db_session())
    init_db(db)
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(
    main_router,
    prefix=settings.API_V1_STR,
)


@app.get("/", operation_id="welcome", response_model=dict[str, str])
async def root():
    return {"message": "Welcome to Project MM API"}


mcp = FastApiMCP(
    app,
    name="Project MM MCP Server",
    description="MCP server for Project MM",
    describe_full_response_schema=True,
    describe_all_responses=True,
)

mcp.mount()
