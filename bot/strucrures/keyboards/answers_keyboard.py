from random import shuffle

from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.db.loader import db


async def generate_answers_keyboard(test_id: int, question_id: int):
    all_data = await db.get_question_by_id(test_id=test_id, question_id=question_id)

    answers = [(i[1], i[2]) for i in all_data]
    shuffle(answers)

    answers_kb = InlineKeyboardBuilder()
    for ans_id, ans in answers:
        answers_kb.button(
            text=ans, 
            callback_data="test:"+str(test_id) + ":question:"+str(question_id) + ":answer:"+str(ans_id)
        )

    answers_kb.button(text="↩️ Вернуться", callback_data="back")

    if len(answers)%2:
        answers_kb.adjust(1)
    else:
        answers_kb.adjust(2, 2, 1)

    return answers_kb.as_markup()
