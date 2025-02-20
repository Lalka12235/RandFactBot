from typing import Callable,Awaitable,Dict,Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from cachetools import

class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self, time_limit: int = 2) -> None:
        

    async def __call__(
            self,
            handler: Callable[[Message,Dict[str,any]],Awaitable[Any]],
            event: Message,
            data: Dict[str,Any]
    ) -> Any:
        pass