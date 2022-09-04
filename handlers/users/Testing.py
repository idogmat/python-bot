from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("questions"))
async def enterTest(message: types.Message):
    await message.answer("Ты начал проходить тест.\n"
                        "Первый вопрос.\n"
                        "Сколько тебе лет?\n")
    await Test.Q1.set()
    # await Test.next()
    # await Test.Q1.first() аналагично
@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Второй вопрос.\n"
                         "Сколько у тебя денег?\n")
    # await Test.Q2.set()
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text
    await message.answer("Спасибо за ваши ответы")
    await message.answer(f"Ответ 1:{answer1}")
    await message.answer(f"Ответ 2:{answer2}")


    await state.reset_state(with_data=False)
    #with_data=False схранит стэйе
