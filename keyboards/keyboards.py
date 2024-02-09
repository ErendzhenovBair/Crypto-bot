from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text ='BTCUSDT')
    kb.button(text ='ETHUSDT')
    kb.button(text ='BNBUSDT')
    kb.button(text ='XRPUSDT')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard=True)
