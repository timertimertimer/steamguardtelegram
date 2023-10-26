import asyncio
import os
from json import load
from steam.guard import SteamAuthenticator
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards import account_list_keyboard
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv
from datetime import datetime
from loguru import logger

load_dotenv()

TOKEN = os.getenv("STEAMGUARD_BOT_TOKEN")
dp = Dispatcher()


@dp.message((CommandStart()) & (F.from_user.username in ['timertimertimer']))
async def command_start_handler(message: Message) -> None:
    logger.info('start')
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=account_list_keyboard)


@dp.callback_query(F.data != 'Add new config')
async def login_handler(callback_query: CallbackQuery):
    callback_data = callback_query.data
    file_path = os.path.join(os.getcwd(), 'creds', f'{callback_data}.json')
    if os.path.exists(file_path):
        steam_guard = SteamAuthenticator(load(
            open(file_path, encoding='utf-8')))
        code = steam_guard.get_code()        
    await callback_query.answer(code)

@dp.callback_query(F.data == 'Add new config')
async def newconf_handler(callback_query: CallbackQuery):
    pass

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    logger.info('steamguard bot started...')
    await dp.start_polling(bot)


if __name__ == '__main__':    
    asyncio.run(main())
