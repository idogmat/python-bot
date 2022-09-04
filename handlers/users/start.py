from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.private_chat import IsPrivate
from loader import dp


@dp.message_handler(CommandStart(),IsPrivate())
async def bot_start(message: types.Message):
    bot_user = await dp.bot.get_me()
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.answer(bot_user)
