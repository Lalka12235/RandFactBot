from typing import Callable,Awaitable,Dict,Any

from aiogram import BaseMiddleware
from aiogram.types import Message

class CheckSubscption(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message,Dict[str,any]],Awaitable[Any]],
            event: Message,
            data: Dict[str,Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member()

        if chat_member.status == 'left':
            await  event.answer(
                
            )