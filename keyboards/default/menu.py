from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Корм")
    ],
    [
        KeyboardButton(text="Игрушки"),
        KeyboardButton(text="Домики")
    ]

    ],
    resize_keyboard=True
)