import asyncio


async def coro_1():
    await asyncio.sleep(1)
    print('coro_1 says, hello coro_2!')


async def coro_2():
    await asyncio.sleep(1)
    print('coro_2 says, hello coro_1!')


async def main():
    await asyncio.create_task(coro_1())
    await asyncio.create_task(coro_2())

asyncio.run(main())

# import asyncio
#
# async def task1():
#     await asyncio.sleep(1)
#     print("Привет из корутины task1")
#
# async def task2():
#     await asyncio.sleep(1)
#     print("Привет из корутины task2")
#
# async def main():
#     await asyncio.create_task(task1())
#     await asyncio.create_task(task2())
#     print
# asyncio.run(main())
