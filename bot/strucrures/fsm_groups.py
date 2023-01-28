from aiogram.fsm.state import StatesGroup, State


class QuestionsState(StatesGroup):
    """
        Состояния для прохождения тестов
    """
    waiting_for_select = State()
    waiting_for_answer = State()
