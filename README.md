# django-stripe

[Техническое задание.](TZ/Test_task_for_Python_developer.md)


# Для разработчиков

## Настройка Django сервера (папка `server`)
Для работы сервиса обязательно необходимы следующие зависимости:

| Зависимость                                            | Версия |
| ------------------------------------------------------ | ------ |
| [Python](https://www.python.org/downloads/)            | 3.11   |
| [Poetry](https://python-poetry.org/docs/#installation) | latest |

1. Создать `.env` файл.

Создать файл можно путем копирования файла `.env.example` с новым названием `.env`.

В файле нужно поменять данные для подключения API Stripe:
* Публичный ключ (ключ `STRIPE_PUBLIC_KEY`)
* Секретный ключ (ключ `STRIPE_SECRET_KEY`)

2. Установить зависимости Python

Для установки зависимостей Python необходимо выполнить команду:
```shell
poetry install
```

3. Выполнить миграции

Сделать это можно следующей командой:
```shell
poetry run python manage.py migrate
```

Далее сервис может быть запущен следующей командой:
```shell
poetry run python manage.py runserver
```

## Запуск используя Docker

Чтобы запустить серверную часть Django и Stripe с помощью Docker, вам необходимо:

1. Создайте образ Docker с помощью Dockerfile

```shell
docker build -t myimage .
```

2. Запустите контейнер из образа Docker и откройте его в сети, чтобы к нему можно было получить доступ с хоста

```shell
docker run -p 8000:8000 myimage
```

