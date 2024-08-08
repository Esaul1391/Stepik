import asyncio
import aiofiles
import aiocsv
import aiofiles.os as aos
from pathlib import Path

DIRECTORY = Path(r'C:\Users\Stas\Desktop\Stepik1\ASINCIO\files\files')


async def read_file(path, semaphore):
    async with semaphore:
        async with aiofiles.open(f'{path}', mode='r') as file:
            num = await file.read()
            if int(num) % 2 == 0:
                return int(num)
            else:
                return 0


async def main():
    semaphore = asyncio.Semaphore(100)
    file_path = [DIRECTORY / file_name for file_name in await aos.listdir(DIRECTORY)]
    tasks = [read_file(path, semaphore) for path in file_path]
    res = await asyncio.gather(*tasks)
    print(sum(res))


asyncio.run(main())