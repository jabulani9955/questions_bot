from random import shuffle

from aiogram import Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import  KeyboardButton
from aiogram.fsm.context import FSMContext
import pandas as pd

from commands.callback_data_states import TestCallbackData
from db.config import GET_QUERIES
from db.db import run_query, connect_to_db, get_all_questions
from strucrures.fsm_groups import QuestionsState


async def questions(message: types.Message, state: FSMContext):
    connection = await connect_to_db()

    with connection.cursor() as cursor:
        cursor.execute(GET_QUERIES["GET_QUESTION_AND_ANSWER"])
        all_questions = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]

    df = pd.DataFrame(all_questions, columns=column_names)

    for i in df['question_id'].unique():
        question_df = df[df['question_id'] == i]
        question_text = question_df['question'].values[0]
        answers = question_df['answer'].tolist()
        shuffle(answers)

        questions_markup = InlineKeyboardBuilder()
        for ans in answers:
            ans_id = question_df[question_df['answer'] == ans]['answer_id'].values[0]
            questions_markup.button(text=ans, callback_data="answer_num_" + str(ans_id))
            b=1
        # questions_markup.button(text=answers[1], callback_data=TestCallbackData(text='Привет', user_id=message.from_user.id))
        # questions_markup.button(text=answers[2], callback_data=TestCallbackData(text='Привет', user_id=message.from_user.id))
        # questions_markup.button(text=answers[3], callback_data=TestCallbackData(text='Привет', user_id=message.from_user.id))
        questions_markup.adjust(1)
        
        await message.answer(question_text, reply_markup=questions_markup.as_markup())
        # await state.set_state(QuestionsState.waiting_for_answer)
        

    cursor.close()
    connection.close()


def generate_questions_and_answers(message: types.Message) -> None:
    ...


async def call_questions(call: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state()

        

    

# async def questions_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
#     await call.message.answer(f"Вопрос №1: {callback_data.text}")
