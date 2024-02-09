import asyncio
import logging

from aiogram import Bot, Dispatcher

from data import config
from handlers import price



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    bot =  Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(price.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
