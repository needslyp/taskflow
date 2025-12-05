# Alembic Migrations for User Service

## Создание миграций

Для создания новой миграции выполните:

```bash
cd services/user_service/app
alembic revision --autogenerate -m "описание изменений"
```

## Применение миграций

Для применения миграций:

```bash
cd services/user_service/app
alembic upgrade head
```

## Откат миграций

Для отката на предыдущую версию:

```bash
cd services/user_service/app
alembic downgrade -1
```

## Просмотр истории миграций

```bash
cd services/user_service/app
alembic history
```

## Важно

- Все таблицы создаются в схеме `user_service`
- Миграции применяются автоматически при запуске сервиса через Docker (если настроено)

