from sqlmodel import Session, SQLModel, create_engine, select

from app.config import settings
from app.models.user import User, UserCreate

from app.models import *

from .users import create_user


engine = create_engine(str(settings.DATABASE_URI))

FIRST_USER_MAIL = "admin@mm.com"
FIRST_USER_PW = "admin1234"


def init_db(session: Session) -> None:
    """
    Initialize the database with the necessary tables and data.
    """
    SQLModel.metadata.create_all(engine)

    # First user
    first_user = session.exec(select(User).where(User.email == FIRST_USER_MAIL)).first()

    if not first_user:
        first_user = UserCreate(
            email=FIRST_USER_MAIL,
            password=FIRST_USER_PW,
        )
        if not create_user(session, first_user):
            raise Exception("Failed to create the first user")
