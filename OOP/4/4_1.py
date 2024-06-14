class Thing:
    __instance_id = 0
    __attrs = ('id', 'name', 'price', 'weight', 'dims', 'memory', 'frm')
    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        self.name = name
        self.price = price
        self.id = self.__get_id()
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    @classmethod
    def __get_id(cls):
        Thing.__instance_id += 1
        return Thing.__instance_id

    def get_data(self):
        return tuple(getattr(self, name) for name in self.__attrs)
class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims

class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm







# class Animal:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
# class Cat(Animal):
#     def __init__(self, name, old, color, weight):
#         super().__init__(name, old)
#         self.color = color
#         self.weight = weight
#
#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.color}, {self.weight}"
#
# class Dog(Animal):
#     def __init__(self, name, old, breed, size):
#         super().__init__(name, old)
#         self.breed = breed
#         self.size = size
#
#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.breed}, {self.size[0]}, {self.size[1]}"
