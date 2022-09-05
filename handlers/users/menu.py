from aiogram.dispatcher.filters import Command, Text
from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите товар ниже", reply_markup=menu)

@dp.message_handler(text="Корм")
async def show_menu(message: types.Message):
    await message.answer("Выбрали Корм")


@dp.message_handler(Text(equals=["Игрушки","Домики"]))
async def show_menu(message: types.Message):
    await message.answer(f"Выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())
    #reply_markup=ReplyKeyboardRemove()-скроет меню