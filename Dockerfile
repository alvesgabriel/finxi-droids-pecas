FROM python:3.8-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY contrib/docker-env .env
RUN pip install -U pip && \
    pip install -U pipenv && \
    pipenv install --system --dev

COPY . /code/
