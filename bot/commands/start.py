from aiogram import types

from bot.strucrures.keyboards import generate_tests_keyboard
from bot.db.loader import db


async def start(message: types.Message) -> None:
    is_exist = await db.is_user_exist(user_id=message.from_user.id)
    tests_markup = await generate_tests_keyboard()
    if not is_exist:
        await db.add_user(
            user_id=message.from_user.id, 
            username=message.from_user.username, 
            first_name=message.from_user.first_name, 
            last_name=message.from_user.last_name
        )
        if message.from_user.first_name:
            await message.answer(f'<b>Добро пожаловать, {message.from_user.first_name}!</b>')
        else:
            await message.answer(f'<b>Добро пожаловать!</b>')

    await message.answer('<b>Пожалуйста, выберите тест.</b>', reply_markup=tests_markup)


async def call_start(call: types.CallbackQuery) -> types.Message:
    """
    Хендлер для команды /start
    :param call:
    :param state:
    """

    tests_markup = await generate_tests_keyboard()
    await call.message.edit_text('<b>Пожалуйста, выберите тест.</b>', reply_markup=tests_markup)
