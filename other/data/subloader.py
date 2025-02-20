import os
from ujson import loads
import aiofiles

async def get_json(filename: str) -> str:
    path = f'data/{filename}'
    if os.path.exists(path):
        async with aiofiles.open(path, 'r',encoding='utf-8') as f:
            return loads(await f.read())
    return []