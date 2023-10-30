from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from data.subloader import accounts


class SteamGuardCode(CallbackData, prefix='code'):
    action: str


def get_codes_fab():
    builder = InlineKeyboardBuilder()
    for account in accounts:
        account_name = account['account_name']
        builder.button(
            text=account_name, callback_data=SteamGuardCode(
                action=account_name)
        )
    builder.adjust(len(accounts))
    return builder.as_markup()
