FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED = 1
WORKDIR /riade/django_docker_student
COPY Pipfile Pipfile.lock /riade/django_docker_student/
RUN pip install pipenv && pipenv install --system
COPY . /riade/django_docker_student/