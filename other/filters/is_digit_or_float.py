from typing import Any

from aiogram.filters import BaseFilter, CommandObject
from aiogram.types import Message

class CheckForDigit(BaseFilter):

    async def __call__(self, message: Message, **data: Any) -> bool:
        command: CommandObject = data.get('coomand')
        arg = command.args

        if arg.isnumeric() or (arg.count('.') == 1 and arg.replace('.','').isnumeric()):
            return True
        return False