from aiogram import Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import  KeyboardButton

from commands.callback_data_states import TestCallbackData
from db.db_commands import get_from_db


async def questions(message: types.Message):
    all_questions = await get_from_db(query="SELECT * FROM questions;")

    for question in all_questions:
        questions_markup = InlineKeyboardBuilder()
        questions_markup.button(text="xuy", url="ya.ru")
        questions_markup.button(text=question[2], callback_data=TestCallbackData(text='Привет', user_id=message.from_user.id))
        questions_markup.adjust(1)
        await message.answer(question[1], reply_markup=questions_markup.as_markup())
        

    

# async def questions_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
#     await call.message.answer(f"Вопрос №1: {callback_data.text}")
