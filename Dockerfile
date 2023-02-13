FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED 1
ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8
RUN mkdir -p /usr/src/app

RUN apt-get update -y && \
    pip install poetry && \
    pip install --upgrade pip

COPY . /usr/src/app
RUN poetry install --no-dev

CMD ['poetry']

# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
