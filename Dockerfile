FROM python:3.11

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    PROJECT_HOME=/home/fastApi

WORKDIR ${PROJECT_HOME}

COPY ./requirements.txt ${PROJECT_HOME}/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ${PROJECT_HOME}/requirements.txt

# Copy project code.
COPY ./main.py ${PROJECT_HOME}/main.py
COPY ./tracking_system ${PROJECT_HOME}/tracking_system

# Copy migration system.
COPY ./alembic ${PROJECT_HOME}/alembic
COPY ./scripts ${PROJECT_HOME}/scripts
COPY ./alembic.ini ${PROJECT_HOME}/alembic.ini

EXPOSE 80
