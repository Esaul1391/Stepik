import asyncio

files = ['image.png', 'file.csv', 'file1.txt']
missed_files = [...]

# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    else:
        await asyncio.sleep(1)
        return f'Файл {file_name} успешно скачан'

# Ваш код пишите тут:
async def main():
    tasks = [download_file(file) for file in files]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, FileNotFoundError):
            print(result)



asyncio.run(main())