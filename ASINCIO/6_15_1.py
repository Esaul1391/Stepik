import asyncio
from itertools import product
import random
shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]

combinations = list(product(shapes, colors, actions))


async def launch_firework(comb: tuple):
    shape, color, action = comb
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")

async def main():
    tasks = [launch_firework(comb) for comb in combinations]
    await asyncio.gather(*tasks)


asyncio.run(main())
