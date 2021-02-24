FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create dir for logs
RUN mkdir -p /app/logs/django/

# requirements setup
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache -r /app/requirements.txt \
    && pip install gunicorn

# copy app code & set workdir
WORKDIR /app/src/
COPY ./src/ /app/src/

# run gunicorn
CMD ["gunicorn", "--bind", "app:8000", "--preload", "--workers", "3", "core.wsgi:application", "--access-logfile", "/app/logs/gunicorn_access.log", "--error-logfile",  "/app/logs/gunicorn_error.log"]
