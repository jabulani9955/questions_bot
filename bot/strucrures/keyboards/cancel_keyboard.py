from aiogram.utils.keyboard import InlineKeyboardBuilder


async def generate_cancel_keyboard():
    cancel_kb = InlineKeyboardBuilder()
    cancel_kb.button(text="↩️ Вернуться", callback_data="backs")
    cancel_kb.adjust(1)
    return cancel_kb.as_markup()
