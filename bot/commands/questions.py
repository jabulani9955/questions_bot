from random import shuffle

from aiogram import types
from aiogram.utils.markdown import code

from bot.strucrures.keyboards.answers_keyboard import generate_answers_keyboard, generate_digits_buttons
from bot.strucrures.keyboards.cancel_keyboard import generate_cancel_keyboard
from bot.db.loader import db
from bot.commands.static_text import SMILES_DIGITS


async def call_questions(call: types.CallbackQuery):
    _, test_id = call.data.split(':')
    n_questions = await db.get_questions_num(test_id=int(test_id))

    # Вызываем первый вопрос.
    all_data = await db.get_question_by_id(test_id=int(test_id), question_num=1)
    question_text = " ".join(all_data[0][0].strip().split())
         
    answers = [(i[1], i[2]) for i in all_data]
    shuffle(answers)
    
    if any(len(i[1]) > 35 for i in answers):
        output_ans = '\n'
        for i, (_, ans) in enumerate(answers, start=1):
            ans = " ".join(ans.strip().split())
            output_ans += f"{SMILES_DIGITS[i]} <code>{ans}</code>\n"
        question_text += output_ans
        markup = await generate_digits_buttons(test_id=int(test_id), question_num=1, answers=answers)
    else:
        markup = await generate_answers_keyboard(test_id=int(test_id), question_num=1)
    await call.message.edit_text(f"Вопрос {1}/{n_questions}:\n<b>{question_text}</b>", reply_markup=markup)


async def call_answers(call: types.CallbackQuery) -> None:
    _, test_id, _, q_num, _, ans_id = call.data.split(':')
    correct_answer = await db.get_correct_answer(test_id=int(test_id), question_num=int(q_num))
    n_questions = await db.get_questions_num(test_id=int(test_id))

    is_correct_answer = int(ans_id) == int(correct_answer[0][1])
    
    await db.add_user_answer(
        user_id=call.from_user.id,
        test_id=int(test_id),
        question_num=int(q_num),
        answer_id=int(ans_id),
        is_correct_answer=is_correct_answer
    )

    all_data = await db.get_question_by_id(
        test_id=int(test_id), 
        question_num=(int(q_num)+1) if int(q_num) < n_questions else 1
    )
    question_text = " ".join(all_data[0][0].split())
    answers = [(i[1], i[2]) for i in all_data]
    shuffle(answers)
    
    # Клавиатура, на которую надо поменять в случае правильного ответа
    if any(len(i[1]) > 35 for i in answers):
        output_ans = '\n'
        for i, (_, ans) in enumerate(answers, start=1):
            ans = " ".join(ans.strip().split())
            output_ans += f"{SMILES_DIGITS[i]} <code>{ans}</code>\n"
        question_text += output_ans
        markup = await generate_digits_buttons(
            test_id=test_id, 
            question_num=int(q_num)+1 if int(q_num) != n_questions else 1, 
            answers=answers
        )
    else:
        markup = await generate_answers_keyboard(
            test_id=int(test_id), 
            question_num=int(q_num)+1 if int(q_num) != n_questions else 1
        )
    finish_markup = await generate_cancel_keyboard()

    if is_correct_answer:
        if int(q_num) == n_questions:
            await call.message.edit_text(
                f"Тест завершен.\nНажмите на кнопку ниже, чтобы вернуться в главное меню.", 
                reply_markup=finish_markup
            )
        else:
            await call.message.edit_text(
                f"Вопрос {int(q_num)+1}/{n_questions}:\n<b>{question_text}</b>", 
                reply_markup=markup
            )
    else:
        await call.answer(text="❌ Ответ неверный! Выберете другой.")
    