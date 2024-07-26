import asyncio


# Объявите функцию publish_post: принимает на вход текст поста и имитирует публикацию нового поста на блоге Васи
async def publish_post(text):
    await asyncio.sleep(0.1)
    print(f"Пост опубликован: {text}")


async def notify_send(s):
    await asyncio.sleep(0.1)
    print(f"Уведомление отправлено {s}")


async def notify_subscribers(subscribers):
    tasks = [notify_send(s) for s in subscribers]
    await asyncio.gather(*tasks)


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    await asyncio.create_task(publish_post(post_text))
    await asyncio.create_task(notify_subscribers(subscribers))


asyncio.run(main())
