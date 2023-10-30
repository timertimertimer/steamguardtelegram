from contextlib import suppress

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from keyboards import fabrics
from data.subloader import accounts
from steam.guard import SteamAuthenticator

router = Router()

@router.callback_query(fabrics.SteamGuardCode.filter(F.action.in_([name['account_name'] for name in accounts])))
async def get_code_handler(call: CallbackQuery, callback_data: fabrics.SteamGuardCode):
    account_name = callback_data.action
    account = list(filter(lambda x: x['account_name'] == account_name, accounts))[0]
    code = SteamAuthenticator(account).get_code()
    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f'<b>{code}</b>',
            reply_markup=fabrics.get_codes_fab()
        )
    await call.answer()