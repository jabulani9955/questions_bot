import os
import psycopg2
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.fsm_storage import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.utils.executor import start_polling

from db.config import DB_PARAMS


# Connect to the PostgreSQL database
# DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(**DB_PARAMS)

# Initialize the Telegram bot and FSM storage
bot = Bot(token="5972508408:AAHGQvqvHaPJx4HPLrxZRhVGcI-_82DGQ5w")
dp = Dispatcher(bot, storage=MemoryStorage())



# Create the inline keyboard for the menu
menu_keyboard = types.InlineKeyboardMarkup()
menu_keyboard.add(types.InlineKeyboardButton("Ask a question", callback_data="ask_question"),
                  types.InlineKeyboardButton("View FAQs", callback_data="view_faqs"),
                  types.InlineKeyboardButton("Answer questions", callback_data="answer_question"))

# menu_keyboard.add(InlineKeyboardButton(text="Ask a question", callback_data="ask_question"),
#                   InlineKeyboardButton(text="View FAQs", callback_data="view_faqs"),
#                   InlineKeyboardButton(text="Answer questions", callback_data="answer_question"))


# Handle the /start command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Welcome to the FAQ bot! Please choose an option from the menu below.", reply_markup=menu_keyboard)
    await dp.current_state(chat=message.chat.id).set_state("menu")


# Handle callback queries from the menu
@dp.callback_query_handler(lambda c: c.data == "ask_question")
async def process_ask_question(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer("Please enter your question.")
    await dp.current_state(chat=callback_query.message.chat.id).set_state("question")


@dp.callback_query_handler(lambda c: c.data == "view_faqs")
async def process_view_faqs(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # Retrieve FAQs from the database and send them to the user
    await callback_query.message.answer("Here are the FAQs: ...")


@dp.callback_query_handler(lambda c: c.data == "answer_question")
async def process_answer_question(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # Retrieve a question from the database and send it to the user with inline buttons for the answers
    question_text = "What is the capital of France?"
    answer_keyboard = types.InlineKeyboardMarkup()
    answer_keyboard.add(types.InlineKeyboardButton("Paris", callback_data="Paris"),
                        types.InlineKeyboardButton("Marseille", callback_data="Marseille"),
                        types.InlineKeyboardButton("Lyon", callback_data="Lyon"),
                        types.InlineKeyboardButton("Nice", callback_data="Nice"))
    await callback_query.message.answer(question_text, reply_markup=answer_keyboard)
    await dp.current_state(chat=callback_query.message.chat.id).set_state("answer")


@dp.callback_query_handler(lambda c: c.data in ["Paris", "Marseille", "Lyon", "Nice"])
async def process_answer(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    # Check if the answer is correct and store the answer in the database
    if answer == "Paris":
        correct = True
    else:
        correct = False

    user_id = callback_query.from_user.id
    # cur = conn.cursor()
    # cur.execute("INSERT INTO answers (user_id, answer, correct) VALUES (%s, %s, %s)", (user_id, answer, correct))
    # conn.commit()
    # cur.close()

    if correct:
        await callback_query.message.answer("Correct! The capital of France is Paris.")
    else:
        await callback_query.message.answer("Incorrect. The capital of France is Paris.")
    await dp.current_state(chat=callback_query.message.chat.id).set_state("menu")


@dp.message_handler(state="question", content_types=Text)
async def process_question(message: types.Message, state: FSMContext):
    question = message.text
    await message.answer("Thank you for your question. It has been added to the FAQ.")
    await state.set_state("menu")


@dp.message_handler()
async def process_other_messages(message: types.Message):
    current_state = dp.current_state(chat=message.chat.id).get_state()
    if current_state is None or current_state == "menu":
        await message.answer("Here is the menu:", reply_markup=menu_keyboard)
    else:
        await message.answer("Invalid input. Please choose an option from the menu.")


start_polling(dp)