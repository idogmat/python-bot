from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("questions", "Пройти тест"),
        types.BotCommand("menu", "Выбрать товар"),
        types.BotCommand("items", "Купить товар"),
    ])
