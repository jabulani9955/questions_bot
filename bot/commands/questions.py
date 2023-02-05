from random import shuffle

from aiogram import types

from bot.strucrures.keyboards.answers_keyboard import generate_answers_keyboard
from bot.strucrures.keyboards.cancel_keyboard import generate_cancel_keyboard
from bot.db.loader import db


async def call_questions(callback: types.CallbackQuery):
    n_questions = await db.get_questions_num()
    
    # Вызываем первый вопрос.
    all_data = await db.get_question_by_id(question_id=1)
    question_text = all_data[0][1]
    
    answers = [(i[2], i[3]) for i in all_data]
    shuffle(answers)
    
    markup = await generate_answers_keyboard(question_id=1)
    await callback.message.edit_text(f"Вопрос {1}/{n_questions}:\n{question_text}", reply_markup=markup)


async def call_answers(call: types.CallbackQuery) -> None:
    _, q_id, _, ans_id = call.data.split(':')
    correct_answer_id = (await db.get_correct_answer(question_id=int(q_id)))[1]
    n_questions = await db.get_questions_num()

    is_correct_answer = int(ans_id) == int(correct_answer_id)
    
    await db.add_user_answer(
        user_id=call.from_user.id,
        question_id=int(q_id),
        answer_id=int(ans_id),
        is_correct_answer=is_correct_answer
    )

    all_data = await db.get_question_by_id(question_id=(int(q_id)+1) if int(q_id) < n_questions else 1)
    question_text = all_data[0][1]

    # Клавиатура, на которую надо поменять в случае правильного ответа
    markup = await generate_answers_keyboard(int(q_id)+1 if int(q_id) != n_questions else 1)
    finish_markup = await generate_cancel_keyboard()

    if is_correct_answer:
        if int(q_id) == n_questions:
            await call.message.edit_text(
                f"Тест завершен. Ваша статистика:\nНажмите на кнопку ниже, чтобы вернуться в главное меню.", 
                reply_markup=finish_markup
            )
        else:
            await call.message.edit_text(
                f"Вопрос {int(q_id)+1}/{n_questions}:\n{question_text}", 
                reply_markup=markup
            )
    else:
        await call.answer(text="❌ Ответ неверный! Выберете другой.")
    