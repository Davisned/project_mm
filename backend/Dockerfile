FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.7.8 /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync --locked

CMD ["uv", "run", "fastapi", "run", "app/main.py"]
