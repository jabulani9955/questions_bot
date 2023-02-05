from random import shuffle

from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.db.loader import db


async def generate_answers_keyboard(question_id: int):
    all_data = await db.get_question_by_id(question_id=question_id)

    answers = [(i[2], i[3]) for i in all_data]
    shuffle(answers)

    answers_kb = InlineKeyboardBuilder()
    for ans_id, ans in answers:
        answers_kb.button(text=ans, callback_data="question:" + str(question_id) + ":" + "answer:" + str(ans_id))

    answers_kb.button(text="↩️ Вернуться", callback_data="back")
    answers_kb.adjust(2, 2, 1)
    return answers_kb.as_markup()
