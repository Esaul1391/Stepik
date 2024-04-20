import asyncio


async def coro_1():
    print("Вызываю корутину 0")


async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()


async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()


async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()


async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()




async def main():
    await asyncio.gather(coro_5())

asyncio.run(main())



# import asyncio
#
#
# async def generate(num):
#     await asyncio.sleep(1)
#     print(f'Корутина generate с аргументом {num}')
#
#
# async def main():
#     for i in range(10):
#         await asyncio.create_task(generate(i))
#
# asyncio.run(main())
