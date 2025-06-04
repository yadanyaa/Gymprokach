# GymProkach

Небольшой веб-сервис с фитнес‑калькуляторами и готовыми программами тренировок.

## Запуск

1. Установите зависимости: `pip install -r requirements.txt`.
2. При необходимости запустите миграции БД: `alembic upgrade head`.
3. Запустите сайт: `python app.py`.
### Docker

```
docker compose up --build
```

## ER-диаграмма

```
User --- Tracker
  |        |
  |        --- result
  --- settings
```
