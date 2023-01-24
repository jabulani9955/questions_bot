from aiogram.filters.callback_data import CallbackData


class TestCallbackData(CallbackData, prefix='text'):
    text: str
    user_id: int
