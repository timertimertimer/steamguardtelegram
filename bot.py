import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import user_commands
from callbacks import steamguardcodes

import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

TOKEN = os.getenv("STEAMGUARD_BOT_TOKEN")
dp = Dispatcher()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    logger.info('steamguard bot started...')
    
    dp.include_routers(
        user_commands.router,
        steamguardcodes.router
    )
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
