from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def calc_kb():
    items = [
        '1','2','3','/', 
        '4','5','6','*',
        '7','8','9','-',
        '0','.','=','+'
    ]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text='НАЗАД')
    builder.adjust(*[4] *4 )

    return builder.as_markup()


def profile(text: str | list):
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    [builder.button(text=txt) for txt in text]

    return builder.as_markup()