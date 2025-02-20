from aiogram.types  import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
)


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Хочу факт'),
            KeyboardButton(text='Закладки'),
            KeyboardButton(text='Рейтинг')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие',
    selective=True
)

save = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Хочу факт'),
            KeyboardButton(text='Сохранить факт'),
            KeyboardButton(text='Рейтинг')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие',
    selective=True
)
