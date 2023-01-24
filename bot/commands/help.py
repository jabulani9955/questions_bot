from aiogram import types
from aiogram.filters.command import CommandObject
from aiogram.handlers import CallbackQueryHandler
from aiogram.types import InlineKeyboardButton

from commands.bot_commands import bot_commands


async def help_command(message: types.Message, command: CommandObject) -> None:
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
                )
        else:
            return await message.answer('Нет такой команды.')
    return help_func(message)
    

async def help_func(message: types.Message) -> None:
    return await message.answer(
        'Помощь и справка о боте.\n'
        'Используй /help <команда>, чтобы получить информацию о команде.\n'
    )


async def call_help_func(call: types.CallbackQuery) -> None:
    await call.message.edit_text(
        'Помощь и справка о боте.\n'
        'Используй /help <команда>, чтобы получить информацию о команде.\n',
        reply_markup=call.message.reply_markup.inline_keyboard.append(
            [InlineKeyboardButton(text='Назад', callback_data='clear')]
        )
    )
