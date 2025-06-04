import asyncio

from aiogram import Bot, Dispatcher

from bot.config import settings
from bot.handlers import commands

async def main() -> None:
    bot = Bot(token=settings.token)
    dp = Dispatcher()
    dp.include_router(commands.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
