

import asyncio

# Инициализация банковского счета
bank_account = 10000
lock = asyncio.Lock()
print(f"Исходный баланс: {bank_account}р")


async def withdraw_money(amount):
    global bank_account
    # Проверка наличия достаточных средств на счете
    print(f"Попытка снять {amount}р. Доступный баланс: {bank_account}р")
    async with lock:
        if bank_account >= amount:
            await asyncio.sleep(0.01)  # Имитация долгой операции
            bank_account -= amount
            print(f"Снятие {amount}р успешно. Оставшийся баланс: {bank_account}р")
        else:
            print(f"Снятие {amount}р не удалось. Недостаточно средств. Оставшийся баланс: {bank_account}р")


async def main():
    tasks = [asyncio.create_task(withdraw_money(1200)) for x in range(9)]
    await asyncio.gather(*tasks)
    print(f'Конечный остаток средств: {bank_account}р')

asyncio.run(main())