FROM --platform=linux/amd64 python:3.10-slim-buster

WORKDIR /app

RUN apt update && apt install -y ffmpeg

RUN pip3 install poetry

COPY poetry.lock pyproject.toml .env ./

RUN poetry config --list && \
    poetry install -vv --no-interaction --no-ansi --no-cache

COPY src/ .

COPY audio/ audio/

CMD ["poetry", "run", "python3", "main.py"]