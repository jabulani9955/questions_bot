from random import shuffle

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import pandas as pd

# from ...commands.questions import get_questions_num
from db.db import get_questions_num, get_question_by_id


async def generate_answers_keyboard(question_id: int):
    # n_questions = await get_questions_num()

    all_data = await get_question_by_id(question_id)

    answers = [(i[2], i[3]) for i in all_data]
    shuffle(answers)

    answers_kb = InlineKeyboardBuilder()
    for ans_id, ans in answers:
        answers_kb.button(text=ans, callback_data="question:" + str(question_id) + ":" + "answer:" + str(ans_id))

    answers_kb.button(text="↩️ Вернуться", callback_data="back")

    answers_kb.adjust(2, 2, 1)
    return answers_kb.as_markup()


async def generate_answers_keyboard_v2():
    """ Эта клавиатура генерирует цифры на кнопках. """
    ...