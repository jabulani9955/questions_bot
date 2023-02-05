from aiogram import types
    

async def help_func(message: types.Message) -> None:
    await message.answer(
        'Отвечай на вопросы!!!\n'
    )
