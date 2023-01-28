from contextlib import suppress

from aiogram import Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import  KeyboardButton
from aiogram.fsm.context import FSMContext

from strucrures.keyboards import MENU_BOARD
from strucrures.fsm_groups import QuestionsState


async def start(message: types.Message) -> None:
    await message.answer('Меню', reply_markup=MENU_BOARD)


async def call_start(call: types.CallbackQuery, state: FSMContext) -> types.Message:
    """
    Хендлер для команды /start
    :param call:
    :param state:
    """
    await state.clear()
    with suppress(Exception):
        await call.message.delete()
    return await call.message.answer('Меню', reply_markup=MENU_BOARD)
# async def menu_questions(message: types.Message, state: FSMContext) -> None:
#     await message.answer(text='Пройти тест')
#     await state.set_state(QuestionsState.waiting_for_select)
