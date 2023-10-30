import aiofiles
import asyncio
from json import loads
from pathlib import Path


async def get_accounts():
    creds_path = Path(Path.cwd(), 'data')
    desired_extensions = ['.json', '.maFile']
    accounts = []
    for file_path in creds_path.iterdir():
        if file_path.suffix in desired_extensions:
            async with aiofiles.open(file_path, encoding='utf-8') as file:
                accounts.append(loads(await file.read()))
    return accounts

accounts = asyncio.run(get_accounts())
