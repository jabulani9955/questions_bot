__all__ = ['register_user_commands', 'bot_commands']


from aiogram.dispatcher.router import Router
from aiogram.filters.command import CommandStart, Command
from aiogram import F

from bot.commands.start import start, call_start
from bot.commands.help import help_func
from bot.commands.bot_commands import bot_commands
from bot.commands.questions import call_questions, call_answers


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_func, Command(commands=['help']))
    router.message.register(start, F.text=='Старт') 

    router.callback_query.register(call_questions, F.data=='take_test')
    router.callback_query.register(call_answers, F.data.startswith('question:'))
    router.callback_query.register(call_start, F.data.startswith('back'))
