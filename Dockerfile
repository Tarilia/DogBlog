FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

WORKDIR /dogblog

RUN pip install --upgrade pip --no-cache-dir && \
    pip install poetry --no-cache-dir && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

COPY . .

FROM base as dev

RUN poetry install --no-interaction --no-ansi


FROM base as prod

RUN poetry install --without dev --no-interaction --no-ansi
