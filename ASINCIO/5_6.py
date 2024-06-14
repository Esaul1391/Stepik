import asyncio

async def check_book(book):
    await asyncio.sleep(0.1)
    if not book["Наличие на полке"]:
        return book
    return None

async def main():
    tasks = [check_book(book) for book in books_json]
    results = await asyncio.gather(*tasks)

    missing_books = [book for book in results if book is not None]

    for book in missing_books:
        print(f'{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]} ({book["Год издания"]})')


asyncio.run(main())