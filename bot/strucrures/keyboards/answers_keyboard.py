from random import shuffle

from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.db.loader import db
from bot.commands.static_text import SMILES_DIGITS


async def generate_answers_keyboard(test_id: int, question_num: int):
    all_data = await db.get_question_by_id(test_id=test_id, question_num=question_num)

    answers = [(i[1], i[2]) for i in all_data]
    shuffle(answers)
    
    answers_kb = InlineKeyboardBuilder()
    for ans_id, ans in answers:
        answers_kb.button(
            text=ans, 
            callback_data="test:"+str(test_id) + ":question:"+str(question_num) + ":answer:"+str(ans_id)
        )

    answers_kb.button(text="↩️ Вернуться", callback_data="back")

    if len(answers)%2:
        answers_kb.adjust(1)
    else:
        answers_kb.adjust(2, 2, 1)
    return answers_kb.as_markup()


async def generate_digits_buttons(test_id: int, question_num: list, answers: list):
    digits_kb = InlineKeyboardBuilder()
    for i, (ans_id, ans) in enumerate(answers, start=1):
        digits_kb.button(
            text=SMILES_DIGITS[i], 
            callback_data="test:"+str(test_id) + ":question:"+str(question_num) + ":answer:"+str(ans_id)
        )
    digits_kb.button(text="↩️ Вернуться", callback_data="back")

    if len(answers)%2:
        digits_kb.adjust(3, 1)
    else:
        digits_kb.adjust(2, 2, 1)
    return digits_kb.as_markup()

