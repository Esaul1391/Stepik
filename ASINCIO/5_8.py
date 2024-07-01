import asyncio


dishes = {
    'Куриный суп': 118,
    'Бефстроганов': 13,
    'Рататуй': 49,
    'Лазанья': 108,
    'Паэлья': 51,
    'Утка по-пекински': 41,
         }

async def cook_dish(name, duration):
    print(f"Приготовление {name} начато.")
    await asyncio.sleep((duration/10))
    print(f"Приготовление {name} завершено. за {duration/10}")


async def main():
    tasks = [asyncio.create_task(cook_dish(task, t)) for task, t in dishes.items()]
    done, pending = await asyncio.wait(tasks, timeout=10)
    print(f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")

asyncio.run(main())





# import asyncio
#
# processors_delays = {
#     'Intel Core i9-11900K': 7.01,
#     'Intel Core i7-11700K': 4.32,
#     'Intel Core i5-11600K': 8.59,
#     'AMD Ryzen 9 5950X': 2.53,
# }
#
#
# async def simulate_processing(delay):
#     await asyncio.sleep(delay)
#
#
# async def main():
#     tasks = [asyncio.create_task(simulate_processing(delay=delay), name=task)
#              for task, delay in processors_delays.items()]
#     done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
#     first_completed_task = done.pop()
#     print(f"Первый завершенный процесс: {first_completed_task.get_name()}")
#
#
# asyncio.run(main())
