import asyncio


async def fetch_log(event):
    await asyncio.sleep(event['delay'])
    print(f"Событие: '{event['event']}' обработано с задержкой {event['delay']} сек.")


async def main():
    tasks = [asyncio.create_task(fetch_log(i)) for i in log_events]
    await asyncio.gather(*tasks)


asyncio.run(main())

