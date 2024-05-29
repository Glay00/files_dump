# fastapi-starter 

Шаблон для проектов на FastAPI и для быстрого старта.

# Инструкция по разворачиванию проекта локально
Команды выполняем из корня проекта.
---
 - Клонируем проект с Github

---
- Переключаемся на тестовую ветку
```bash
git checkout dev
```

---
- Затем необходимо скопировать и переименовать файл `.env.example` в файл `.env` и внести необходимые см. [переменные проекта](##Переменные проекта).

---
- Устанавливаем [Poetry](https://python-poetry.org/docs/) для создания виртуального окружения.
```bash
pip install poetry
```

---
- Создаём виртуальное окружение при помощи Poetry.
```bash
poetry env use python 3.11 или poetry env use python 3.12
```

---
- Активируем виртуальное окружение при помощи Poetry
```bash
poetry shell
```

---
- Устанавливаем необходимые dependencies из файла ```poetry.lock``` [Installing-with-poetrylock](https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock).
```bash
pip install poetry --no-root
```

---
-  Сборка контейнера происходит через [docker-compose](https://docs.docker.com/) командой
```bash
docker-compose build
```

---
-  Запуск контейнера происходит через [docker-compose](https://docs.docker.com/) командой
```bash
docker-compose up
```

## Переменные проекта

Структура описания: `Наименование переменной` - Описание переменной - `Пример`

### База данных Postgres

---
`DB_NAME` - наименование базы данных Postgres - database

---
`DB_USER` - наименование пользователя базы данных Postgres - postgres

---
`DB_PASSWORD` - пароль пользователя базы данных Postgres - postgres

---
`DB_HOST` - хост базы данных Postgres для подключения - 0.0.0.0 или 127.0.0.1 (localhost)

---
`DB_PORT` - порт базы данных Postgres для подключения - 6432


## Зависимости:
- Python 3.12
- FastAPI 0.109.0
- Docker
- PostgreSQL 15.3 (через Docker)

## Подключенные фичи/dependencies:
- [Uvicorn](https://www.uvicorn.org/)
- [Sqlalchemy](https://www.sqlalchemy.org/) 
- [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) 
- [Pydantic-settings](https://docs.pydantic.dev/latest/api/pydantic_settings/) 
- [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [Asyncpg](https://magicstack.github.io/asyncpg/current/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Autoflake](https://pypi.org/project/autoflake/)
- [Ruff](https://docs.astral.sh/ruff/)

### Файлы `.env` и `.env.example`
В файле `.env` хранятся переменные среды проекта - этот файл добавлен в гит-игнор (т.к. переменные содержат чувствительную информацию и не должны попасть в историю репозитория).

А файл `.env.example` - это пример как заполнять `.env` с перечнем всех нужных переменных, но с заглушками в значениях (например, `""`).

При старте проекта нужно в корне создать файл `.env` и заполнить его. Если проект уже начат - лучше взять файл у коллег по проекту.

Когда в `.env` изменяется состав переменных **нужно обновить** переменные в `.env.example` - чтобы не потерять какие настройки есть в проекте.

### Файл `version`
В файле указывается номер версии для сборки docker-образа бэкенда.
Версией может быть любая строка, но лучше придерживаться принципа [SemVer](https://semver.org/)

Например `3.4.1`.