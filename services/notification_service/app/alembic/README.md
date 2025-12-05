# Alembic Migrations for Notification Service

## Создание миграций

Для создания новой миграции выполните:

```bash
cd services/notification_service/app
alembic revision --autogenerate -m "описание изменений"
```

## Применение миграций

Для применения миграций:

```bash
cd services/notification_service/app
alembic upgrade head
```

## Откат миграций

Для отката на предыдущую версию:

```bash
cd services/notification_service/app
alembic downgrade -1
```

## Просмотр истории миграций

```bash
cd services/notification_service/app
alembic history
```

## Важно

- Все таблицы создаются в схеме `notification_service`
- Миграции применяются автоматически при запуске сервиса через Docker (если настроено)

