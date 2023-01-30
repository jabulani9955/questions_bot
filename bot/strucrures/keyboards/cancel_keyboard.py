from random import shuffle

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
# import pandas as pd

# from ...commands.questions import get_questions_num
# from db.db import get_questions_num, get_question_by_id


async def generate_cancel_keyboard():
    cancel_kb = InlineKeyboardBuilder()
    
    cancel_kb.button(text="↩️ Вернуться", callback_data="backs")

    cancel_kb.adjust(1)
    return cancel_kb.as_markup()


async def generate_answers_keyboard_v2():
    """ Эта клавиатура генерирует цифры на кнопках. """
    ...