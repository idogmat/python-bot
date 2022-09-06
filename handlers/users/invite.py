from datetime import datetime, timedelta
from aiogram.types import Message
from loader import dp, bot
from aiogram.methods import create_chat_invite_link


@dp.message_handler(text="initChatId")
async def cmd_test(message: Message):
    await bot.send_message(message.chat.id, f"Thanks for adding me!!{message.chat.id}")

@dp.message_handler(text="invite")
async def cmd_test(message: Message):
    chat_id = 1239595678
    expire_date = datetime.now() + timedelta(days=1)
    link = await bot.CreateChatInviteLink(chat_id)

    await message.answer(link.invite_link)
