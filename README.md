# TaskFlow — Сервис для отслеживания задач и проектов

## О проекте

Этот репозиторий содержит несколько микросервисов на FastAPI, связанных с работой пользователей, проектами, уведомлениями и аналитикой. Все сервисы используют PostgreSQL в качестве базы данных и могут быть запущены через Docker Compose.

## Требования

### Для запуска через Docker (рекомендуется)

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (включает Docker Compose)
- Минимум 4 GB свободной оперативной памяти
- Минимум 2 GB свободного места на диске

### Для локальной разработки

- Python 3.14+
- [Pipenv](https://pipenv.pypa.io/en/latest/) для управления зависимостями
- PostgreSQL 16+ (или используйте Docker только для PostgreSQL)

## Структура проекта

```
taskflow/
├── docker/
│   └── docker-compose.yml      # Конфигурация Docker Compose для всех сервисов
├── services/
│   ├── project_service/        # Сервис управления проектами
│   ├── user_service/           # Сервис управления пользователями
│   ├── notification_service/   # Сервис уведомлений
│   └── project_analytics_service/  # Сервис аналитики проектов
├── libs/                       # Общие библиотеки
├── scripts/                    # Вспомогательные скрипты
└── tests/                      # Общие тесты
```

## Быстрый старт

### Вариант 1: Запуск через Docker (рекомендуется)

Этот способ запускает все сервисы и PostgreSQL в контейнерах Docker.

#### Требования

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) установлен и запущен
- Docker Compose (входит в Docker Desktop)

#### Шаги запуска

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/needslyp/taskflow.git
    cd taskflow
    ```

2. Перейдите в папку `docker`:

    ```bash
    cd docker
    ```

3. Запустите все сервисы:

    ```bash
    docker compose up --build
    ```

    При первом запуске это может занять несколько минут, так как Docker будет собирать образы.

4. После успешного запуска сервисы будут доступны по следующим адресам:

    - **project_service**: http://localhost:8001
    - **user_service**: http://localhost:8002
    - **notification_service**: http://localhost:8003
    - **project_analytics_service**: http://localhost:8004
    - **PostgreSQL**: localhost:5432

5. Swagger документация доступна по адресу `/docs` для каждого сервиса:
   - http://localhost:8001/docs
   - http://localhost:8002/docs
   - http://localhost:8003/docs
   - http://localhost:8004/docs

#### Управление Docker контейнерами

- **Остановить все сервисы**: `Ctrl+C` в терминале или `docker compose down`
- **Запустить в фоновом режиме**: `docker compose up -d`
- **Просмотр логов**: `docker compose logs` или `docker compose logs <service_name>`
- **Пересобрать образы**: `docker compose up --build`
- **Остановить и удалить контейнеры**: `docker compose down`
- **Остановить и удалить контейнеры с данными**: `docker compose down -v` (⚠️ удалит данные PostgreSQL)

### Вариант 2: Локальный запуск (для разработки)

Для разработки отдельных сервисов можно запускать их локально.

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/needslyp/taskflow.git
    cd taskflow
    ```

2. Перейдите в папку нужного микросервиса:

    ```bash
    cd services/user_service
    ```

3. Установите зависимости через pipenv:

    ```bash
    pipenv install
    ```

4. Активируйте виртуальное окружение:

    ```bash
    pipenv shell
    ```

5. Убедитесь, что PostgreSQL запущен и доступен (или используйте Docker только для PostgreSQL):

    ```bash
    docker compose -f ../docker/docker-compose.yml up postgres -d
    ```

6. Запустите сервис:

    ```bash
    uvicorn app.main:app --reload
    ```

## База данных PostgreSQL

Проект использует PostgreSQL 16 в качестве основной базы данных. При запуске через Docker Compose база данных автоматически создается и настраивается.

### Параметры подключения

- **Host**: `localhost` (при подключении извне Docker) или `postgres` (изнутри Docker сети)
- **Port**: `5432`
- **User**: `taskflow`
- **Password**: `taskflow`
- **Database**: `taskflow_db`

### Подключение к базе данных

#### Способ 1: Через Docker контейнер (рекомендуется)

```bash
cd docker
docker compose exec postgres psql -U taskflow -d taskflow_db
```

После подключения вы можете выполнять SQL команды:
- `\dt` - показать все таблицы
- `\d <table_name>` - показать структуру таблицы
- `\q` - выйти из psql

#### Способ 2: Через внешний клиент

Используйте любой PostgreSQL клиент (например, pgAdmin, DBeaver, DataGrip) с параметрами:

- **Host**: `localhost`
- **Port**: `5432`
- **Username**: `taskflow`
- **Password**: `taskflow`
- **Database**: `taskflow_db`

#### Способ 3: Через командную строку (если установлен PostgreSQL клиент)

```bash
psql -h localhost -p 5432 -U taskflow -d taskflow_db
```

При запросе пароля введите: `taskflow`

### Полезные команды для работы с базой данных

```bash
# Подключиться к базе данных
docker compose exec postgres psql -U taskflow -d taskflow_db

# Выполнить SQL команду напрямую
docker compose exec postgres psql -U taskflow -d taskflow_db -c "SELECT version();"

# Создать резервную копию базы данных
docker compose exec postgres pg_dump -U taskflow taskflow_db > backup.sql

# Восстановить базу данных из резервной копии
docker compose exec -T postgres psql -U taskflow taskflow_db < backup.sql
```

## Управление секретами и зависимостями

- Все переменные окружения хранятся в `.env` файлах внутри сервисов.
- Зависимости для каждого сервиса определяются через `Pipfile` и `Pipfile.lock`.
- При запуске через Docker переменные окружения настраиваются автоматически через `docker-compose.yml`.

## Микросервисы

Проект состоит из следующих микросервисов:

| Сервис | Порт (Docker) | Описание |
|--------|---------------|----------|
| `project_service` | 8001 | Управление проектами |
| `user_service` | 8002 | Управление пользователями |
| `notification_service` | 8003 | Система уведомлений |
| `project_analytics_service` | 8004 | Аналитика по проектам |

Все сервисы используют общую базу данных PostgreSQL и могут взаимодействовать друг с другом через HTTP API.

## Разработка и тестирование

- Тесты для сервисов лежат в директориях `services/<имя_сервиса>/tests` и в общем `tests/`.
- Для запуска тестов используйте:

    ```bash
    pipenv run pytest
    ```

- При разработке рекомендуется использовать локальный запуск сервисов с `--reload` флагом для автоматической перезагрузки при изменениях.
- Для тестирования интеграции с базой данных используйте Docker Compose для запуска PostgreSQL:

    ```bash
    cd docker
    docker compose up postgres -d
    ```

## Как добавить новый микросервис

1. Создайте новую директорию внутри `services/`.
2. Скопируйте базовую структуру из существующего сервиса.
3. Настройте `Pipfile`, `.env`, тесты и основное приложение FastAPI по образцу.

## Документация

- Swagger/OpenAPI документация автоматически доступна по адресу `/docs` у каждого запущенного сервиса.
- При запуске через Docker документация доступна по следующим адресам:
  - http://localhost:8001/docs - project_service
  - http://localhost:8002/docs - user_service
  - http://localhost:8003/docs - notification_service
  - http://localhost:8004/docs - project_analytics_service
- Альтернативная документация ReDoc доступна по адресу `/redoc` для каждого сервиса.

## Gitignore

- Файл `.gitignore` настроен для игнорирования секретов, виртуальных окружений, временных файлов, логов и артефактов тестов.

## Лицензия

**MIT License**

## Авторы

**needslyp**

---
