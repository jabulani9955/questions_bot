from contextlib import suppress

from aiogram import Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import  KeyboardButton
from aiogram.fsm.context import FSMContext

from strucrures.keyboards import MENU_BOARD
from strucrures.fsm_groups import QuestionsState
from db.db import is_user_exist, add_user


async def start(message: types.Message) -> None:
    is_exist = await is_user_exist(message.from_user.id)
    
    if not is_exist:
        await add_user(
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


async def call_start(call: types.CallbackQuery, state: FSMContext) -> types.Message:
    """
    Хендлер для команды /start
    :param call:
    :param state:
    """
    # await state.clear()
    # with suppress(Exception):
    #     await call.message.delete()
    return await call.message.edit_text('<b>МЕНЮ</b>', reply_markup=MENU_BOARD)
# async def menu_questions(message: types.Message, state: FSMContext) -> None:
#     await message.answer(text='Пройти тест')
#     await state.set_state(QuestionsState.waiting_for_select)
