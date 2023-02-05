from aiogram import types

from bot.strucrures.keyboards import MENU_BOARD
from bot.db.loader import db


async def start(message: types.Message) -> None:
    is_exist = await db.is_user_exist(user_id=message.from_user.id)
    
    if not is_exist:
        await db.add_user(
            user_id=message.from_user.id, 
            username=message.from_user.username, 
            first_name=message.from_user.first_name, 
            last_name=message.from_user.last_name
        )
        await message.answer(f'Добро пожаловать, <b>{message.from_user.first_name}</b>')
        await message.answer('<b>МЕНЮ</b>', reply_markup=MENU_BOARD)
    else:
        await message.answer(f'Давно не виделись, <b>{message.from_user.first_name}</b>')
        await message.answer('<b>МЕНЮ</b>', reply_markup=MENU_BOARD)


async def call_start(call: types.CallbackQuery) -> types.Message:
    """
    Хендлер для команды /start
    :param call:
    :param state:
    """
    return await call.message.edit_text('<b>МЕНЮ</b>', reply_markup=MENU_BOARD)
