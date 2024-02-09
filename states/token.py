from aiogram.fsm.state import State, StatesGroup

class Token(StatesGroup):
    pair = State()
    quantity = State()
