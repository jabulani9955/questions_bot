from aiogram import Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import  KeyboardButton


async def start(message: types.Message) -> None:
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(
        text="Помощь"
    )
    menu_builder.add(
        KeyboardButton(text='Отправить контакт', request_contact=True)
    )
    await message.answer(
        'Меню', 
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )
