import random
import asyncio

ipaddress = '192.168.0.1'
ports = [i for i in range(80, 86)]
st_port = 80
en_port = 85


async def scan_port(address, port):
    randnumber = random.random()
    await asyncio.sleep(randnumber)
    result = []
    if randnumber < 0.5:
        print(f'Порт {port} на адресе {address} открыт')
        result.append('Порт открыт')
    else:
        print(f'Порт {port} на адресе {address} закрыт')
        result.append('Порт закрыт')
    return result


async def scan_range(address, start_port, end_port):
    print(f"Сканирование портов с {start_port} по {end_port} на адресе {address}")
    tasks = []
    open_ports = []

    for i in range(st_port, en_port):
        task = asyncio.create_task(scan_port(address, i))
        tasks.append(task)
        s = await task
        res = await asyncio.gather(*tasks)
        if s == ['Порт открыт']:
            open_ports.append(i)
        if res:
            print(f'Открытые порты на {address}: {open_ports}')
        else:
            print(f'Открытых портов на {address} не найдено')


asyncio.run(scan_range(ipaddress, st_port, en_port))