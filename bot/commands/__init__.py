__all__ = ['register_user_commands', 'bot_commands']


from aiogram.dispatcher.router import Router
from aiogram.filters.command import CommandStart, Command
from aiogram import F
# from aiogram.fsm.state import any_state

from commands.start import start, call_start
from commands.help import help_command, help_func, call_help_func
from commands.bot_commands import bot_commands
from commands.settings import settings_command, settings_callback
from commands.callback_data_states import TestCallbackData
from commands.questions import call_questions, call_answers
from strucrures.fsm_groups import QuestionsState
 
# from middlewares.register_check import RegisterCheck


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_func, Command(commands=['help']))
    router.message.register(start, F.text=='Старт')
    router.message.register(help_func, F.text=='Помощь')
    # router.message.register(call_questions, Command(commands=['questions']))
    

    router.message.register(settings_command, Command(commands=['settings']))
    router.callback_query.register(call_questions, F.data=='take_test')

    router.callback_query.register(call_help_func, F.data == 'help')
    router.callback_query.register(settings_callback, TestCallbackData.filter())
    router.callback_query.register(call_answers, F.data.startswith('question:'))
    router.callback_query.register(call_start, F.data.startswith('back'))
    
    # router.callback_query.register(call_questions, F.data == 'take_test')
    

    # router.message.register(RegisterCheck)
    # router.callback_query.register(RegisterCheck)
    

    
    
