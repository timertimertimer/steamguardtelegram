from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.fabrics import get_codes_fab
from filters.is_admin import IsAdmin

router = Router()

@router.message(CommandStart(), IsAdmin([222215932, 674509926]))
async def start(message: Message):
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>!", reply_markup=get_codes_fab())