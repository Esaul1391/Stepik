import asyncio

async def countdown(name, seconds):
    pass

async def main():
    treasure_hunt = asyncio.create_task(countdown("Квест на поиск сокровищ", 10))
    dragon_escape = asyncio.create_task(countdown("Побег от дракона", 5))
    await asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())