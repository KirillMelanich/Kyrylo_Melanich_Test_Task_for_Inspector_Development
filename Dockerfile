FROM python:3.11.0-slim-buster

LABEL maintainer = "kirillmelanich@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

#USER django-user
# Dockerfile for the Django application
#FROM python:3.11.0-slim-buster
#
#LABEL maintainer="kirillmelanich@gmail.com"
#
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /app
#
#COPY requirements.txt requirements.txt
#
#RUN apt-get update \
#    && apt-get -y install libpq-dev gcc
#
#RUN pip install -r requirements.txt
#
#COPY . .
#
#RUN mkdir -p /vol/web/media
#
#RUN adduser --disabled-password --no-create-home django-user
#
#RUN chown -R django-user:django-user /vol/
#RUN chmod -R 755 /vol/web/
#
#USER django-user
#
## Dockerfile for the FastAPI service
#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
#
#COPY . .
#
#RUN pip install requests
#
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
