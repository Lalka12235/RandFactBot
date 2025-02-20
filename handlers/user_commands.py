from aiogram import Router
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message

from keyboards import reply



router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')
    await message.answer(f'Хочешь узнать интересный факт?', reply_markup=reply.main)

@router.message(Command('pay'))
async def pay_the_order(message: Message, command: CommandObject) -> None:
    await message.answer('Вы успешно оплатили товар')