from datetime import datetime, timedelta
from aiogram.types import Message

from filters.private_chat import IsPrivate
from loader import dp, bot



@dp.message_handler(text="initChatId")
async def cmd_test(message: Message):
    await bot.send_message(message.chat.id, f"Thanks for adding me!!{message.chat.id}")

@dp.message_handler(IsPrivate(),text="invite")
async def cmd_test(message: Message):
    chat_id = -1001219346081
    expire_date = datetime.now() + timedelta(days=1)
    link = await bot.export_chat_invite_link(chat_id)
    await message.answer(link)
