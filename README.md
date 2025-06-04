# GymProkach Bot

Телеграм-бот с фитнес-инструментами: расчёт калорий, программы тренировок и учёт прогресса.

## Запуск

1. Скопируйте `.env.example` в `.env` и укажите токен бота.
2. Установите зависимости: `pip install -r requirements.txt`.
3. Запустите миграции БД (если нужны): `alembic upgrade head`.
4. Запустите бота: `python bot/main.py`.

5. Запустите веб-сайт: `python app.py`.
### Docker

```
docker compose up --build
```

Бот ответит на `/ping` словом `pong`.

### .env пример

```
TOKEN=<токен_бота>
ADMIN_ID=<telegram id администратора>
```

## ER-диаграмма

```
User --- Tracker
  |        |
  |        --- result
  --- settings
```

## Добавление команд

Новые команды регистрируются в `bot/handlers/commands.py` через декоратор `@router.message(Command("name"))`. Добавьте функцию-обработчик и импортируйте сервисы при необходимости.
