from json import load
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pathlib import Path

creds_path = Path(Path.cwd(), 'creds')
desired_extensions = ['.json', '.maFile']
accounts = []
for file_path in creds_path.iterdir():
    if file_path.suffix in desired_extensions:
        accounts.append(load(open(file_path))['account_name'])
accounts.sort()

accounts.append('Add new config')

account_list_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=el, callback_data=el)
        ] for el in accounts
    ]
)
