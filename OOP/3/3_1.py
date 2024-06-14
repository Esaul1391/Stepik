class Book:
    attrs = {'title': str, 'author': str, 'pages': int, 'year': int}

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.attrs and self.attrs[key] == type(value):
            super().__setattr__(key, value)
        else:
            raise TypeError('Неверный тип присвоенных данных.')


book = Book("Сергей Балакирев", 'Python ООП', 123, 2022)
