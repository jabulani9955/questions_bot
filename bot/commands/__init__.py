__all__ = ['register_user_commands', 'bot_commands']


from aiogram.dispatcher.router import Router
from aiogram.filters.command import CommandStart, Command
from aiogram import F

from commands.start import start
from commands.help import help_command, help_func, call_help_func
from commands.bot_commands import bot_commands
from commands.settings import settings_command, settings_callback
from commands.callback_data_states import TestCallbackData
from commands.questions import questions

# from middlewares.register_check import RegisterCheck


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(help_func, F.text=='Помощь')
    router.message.register(settings_command, Command(commands=['settings']))
    router.message.register(questions, Command(commands=['questions']))

    router.callback_query.register(call_help_func, F.data=='help')
    router.callback_query.register(settings_callback, TestCallbackData.filter())

    # router.message.register(RegisterCheck)
    # router.callback_query.register(RegisterCheck)
    

    
    
