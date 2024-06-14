class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return  hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, things=None):
        things = {} if things is None else things

        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        if things and not all(isinstance(key, Thing) for key in things):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(things)


    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)

# class ListInteger(list):
#     def __init__(self, lst):
#         for x in lst:
#             self.__check_type(x)
#         super().__init__(lst)
#
#     @staticmethod
#     def __check_type(x):
#         if not isinstance(x, int):
#             raise TypeError('можно передавать только целочисленные значения')
#
#     def __setitem__(self, key, value):
#         self.__check_type(value)
#         super().__setitem__(key, value)
#
#     def append(self, value):
#         self.__check_type(value)
#         super().append(value)
