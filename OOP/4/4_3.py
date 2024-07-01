class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = 'леворульный' if True else 'праворульный'

# class Book:
#     def __init__(self, title, author, pages, year):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#
# class DigitBook(Book):
#     def __init__(self, title, author, pages, year, size, frm):
#         super().__init__(title, author, pages, year)
#         self.size =size
#         self.frm = frm
