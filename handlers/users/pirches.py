import logging

from aiogram.dispatcher.filters import Command, Text
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.choice_buttons import choice, pear_keyboard
from keyboards.inline.callback_data import buy_callback
from loader import dp, bot

@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer("На продажу у нас есть 2 товара: 5 груш и 5 яблок\n"
                         "Нажмите отмену, если нечего не нужно", reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    await bot.answer_callback_query(callback_query_id=call.id, cache_time=60)
    # await call.answer(cache_time=60)

    quantity = callback_data.get("quantity")
    await call.message.answer(f"вы выбрали купить грушу.Всего {quantity}.Спасибо", reply_markup=pear_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    await bot.answer_callback_query(callback_query_id=call.id, cache_time=60)
    # await call.answer(cache_time=60)

    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали купить яблоко.Всего {quantity}.Спасибо", reply_markup=pear_keyboard)

@dp.callback_query_handler(text="cancel")
async def buying_pear(call: CallbackQuery):
    await call.answer("Отменили покупку", show_alert=True)

