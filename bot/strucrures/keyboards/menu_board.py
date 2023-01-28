from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


MENU_BOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пройти тест', callback_data='take_test')]
    ]
)
