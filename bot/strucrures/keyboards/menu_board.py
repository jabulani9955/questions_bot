from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MENU_BOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пройти тест', callback_data='take_test')]
    ]
)
