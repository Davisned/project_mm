from sqlmodel import SQLModel


class Token(SQLModel):
    """
    Token model for authentication
    """

    access_token: str
    token_type: str = "bearer"


class TokenPayload(SQLModel):
    """
    Token payload model
    """

    sub: str
