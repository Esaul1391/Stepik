import asyncio


async def async_operation():
    try:
        print("Начало асинхронной операции.")
        await asyncio.sleep(2)
        print("Асинхронная операция успешно завершилась.")
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")


async def main():
    print("Главная корутина запущена.")
    future = asyncio.ensure_future(async_operation())
    await asyncio.sleep(0.1)
    print("Попытка отмены Future.")
    future.cancel()
    try:
        result = await future
        print("Результат Future:", result)
    except asyncio.CancelledError:
        print("Обработка исключения: Future был отменен.")
    if future.cancelled():
        print("Проверка: Future был отменен.")
    else:
        print("Проверка: Future не был отменен.")
    print("Главная корутина завершена.")

asyncio.run(main())











# import asyncio
#
#
# async def set_future_result(value, delay):
#     print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
#     await asyncio.sleep(delay)
#     print("Результат установлен.")
#     return value
#
#
# async def create_and_use_future():
#     future = asyncio.ensure_future(set_future_result("Успех", 2))
#     if not future.done():
#         print("Состояние Future до выполнения: Ожидание")
#     else:
#         print("Состояние Future до выполнения: Завершено")
#     await future
#     print("Задача запущена, ожидаем завершения...")
#     if not future.done():
#         print("Состояние Future до выполнения: Завершено")
#     else:
#         print("Состояние Future до выполнения: Ожидание")
#
#     return future.result()
#
#
# async def main():
#     result = await create_and_use_future()
#     print("Результат из Future:", result)
#
#
# asyncio.run(main())
