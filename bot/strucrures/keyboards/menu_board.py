from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.db.loader import db


async def generate_tests_keyboard():
    all_tests = await db.get_tests_list()
    tests = [(i[0], i[1]) for i in all_tests]
    tests_kb = InlineKeyboardBuilder()
    for test_id, test_name in tests:
        tests_kb.button(text=f"{test_id}. {test_name}", callback_data="start_test:" + str(test_id))
    tests_kb.adjust(1)
    return tests_kb.as_markup()
