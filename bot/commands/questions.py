from random import shuffle

import pandas as pd
import asyncio
from aiogram import Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import  KeyboardButton
from aiogram.fsm.context import FSMContext

from strucrures.keyboards.answers_keyboard import generate_answers_keyboard
from strucrures.keyboards.cancel_keyboard import generate_cancel_keyboard
from commands.callback_data_states import TestCallbackData
from db.config import GET_QUERIES
from db.db import (
    run_query, 
    connect_to_db,
    get_correct_answer, 
    get_questions_num, 
    get_question_by_id,
    add_user,
    add_user_answer
)
from strucrures.fsm_groups import QuestionsState
from strucrures.keyboards import MENU_BOARD


# df = asyncio.run(run_query(GET_QUERIES['GET_QUESTION_AND_ANSWER']))

async def get_all_answers():
    connection = await connect_to_db()

    with connection.cursor() as cursor:
        cursor.execute(GET_QUERIES["GET_ALL_ANSWERS"])
        all_questions = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]

    df = pd.DataFrame(all_questions, columns=column_names)
    return df


async def call_questions(callback: types.CallbackQuery):
    n_questions = await get_questions_num()
    # print(n_questions)

    all_data = await get_question_by_id(1)
    question_text = all_data[0][1]
    
    answers = [(i[2], i[3]) for i in all_data]
    shuffle(answers)
    
    markup = await generate_answers_keyboard(1)
    await callback.message.edit_text(f"Вопрос {1}/{n_questions}:\n{question_text}", reply_markup=markup)


async def get_questions_and_answers(message: types.Message) -> None:
    ...


async def call_answers(call: types.CallbackQuery) -> None:
    _, q_id, _, ans_id = call.data.split(':')
    correct_answer, correct_answer_id = await get_correct_answer(question_id=q_id)
    n_questions = await get_questions_num()

    is_correct_answer = int(ans_id) == int(correct_answer_id)

    # TODO: УЗНАТЬ КАК ПОЛУЧИТЬ ВСЕ ОТВЕТЫ ЗА ТЕКУЩУЮ СЕССИЮ
    
    await add_user_answer(
        user_id=call.from_user.id,
        question_id=q_id,
        answer_id=ans_id,
        is_correct_answer=is_correct_answer
    )

    all_data = await get_question_by_id((int(q_id)+1) if int(q_id) < n_questions else 1)
    question_text = all_data[0][1]

    # await call.message.answer(text=str(n_questions))
    # Клавиатура, на которую надо поменять в случае правильного ответа
    markup = await generate_answers_keyboard(int(q_id)+1 if int(q_id) != n_questions else 1)
    finish_markup = await generate_cancel_keyboard()



    if is_correct_answer:
        # await call.answer(text="✅")
        # await call.message.answer(text=question_text, reply_markup=markup)
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
        
        # await call.message.edit_caption(caption="1", reply_markup=markup)
    else:
        await call.answer(text="❌ Ответ неверный! Выберете другой.")
    
