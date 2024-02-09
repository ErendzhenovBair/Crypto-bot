from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from binance import AsyncClient
from binance.exceptions import BinanceAPIException

from data import config
from keyboards.keyboards import get_keyboard
from states.token import Token

router = Router()


@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите торговую пару.",
        reply_markup=get_keyboard()
    )
    await state.set_state(Token.pair)


@router.message(
        Token.pair,
        F.text.in_(config.AVAILABLE_TOKENS)
)
async def handle_pair_selection(
        message: types.Message, state: FSMContext):
    await state.update_data(selected_pair=message.text)
    await message.answer(
        "Введите количество токенов для определения цены:"
    )
    await state.set_state(Token.quantity)

@router.message(Token.quantity)
async def handle_total_price(message: types.Message, state: FSMContext):
    try:
        await state.update_data(quantity=message.text)
        data = await state.get_data()
        pair = data['selected_pair']
        price = await get_token_price(pair)
        quantity = float(data['quantity'])
        total_price = price * quantity
        formatted_total_price = round(total_price, 2)
        await message.answer(
            f"Общая цена ваших токенов {pair[:-4]} "
            f"на текущий момент: {formatted_total_price} USDT"
        )
        await state.clear()
    except ValueError:
        await message.answer(
            "Некорректное количество. Пожалуйста, введите число."
        )

@router.message()
async def get_token_price(coin: str):
    try:
        binance_client = AsyncClient()
        token_data = await binance_client.get_ticker(symbol=coin)
        return float(token_data['lastPrice'])
    except BinanceAPIException:
        raise ValueError("Пара не найдена")
