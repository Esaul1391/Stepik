class AttrsNumberObject:
    def __init__(self, **kwargs):
        self._attrs_num = 1  # начальное количество атрибутов
        for key, value in kwargs.items():
            setattr(self, key, value)  # установка атрибутов

    def __setattr__(self, name, value):
        if name != '_attrs_num':  # проверка на имя атрибута
            if not hasattr(self, name):  # если атрибут еще не существует
                self._attrs_num += 1  # увеличиваем счетчик
        super().__setattr__(name, value)  # вызываем родительский __setattr__

    def __delattr__(self, name):
        if hasattr(self, name):  # если атрибут существует
            self._attrs_num -= 1  # уменьшаем счетчик
        super().__delattr__(name)  # вызываем родительский __delattr__

    def __getattribute__(self, name):
        if name == 'attrs_num':
            return super().__getattribute__('_attrs_num')  # возвращаем значение атрибута attrs_num
        return super().__getattribute__(name)

music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)



# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __getattribute__(self, name):
#         if name == 'name':
#             return object.__getattribute__(self, 'name').title()
#         elif name == 'total':
#             return object.__getattribute__(self, 'price') * object.__getattribute__(self, 'quantity')
#         else:
#             return object.__getattribute__(self, name)
#
#     # def __getattribute__(self, item):
#     #     if item == self._name:
#     #         return object.__getattribute__(self, item.capitalize())
#     #     return object.__getattribute__(self, item)






# class Const:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             object.__setattr__(self, key, value)
#
#
#     def __getattribute__(self, item):
#         return object.__getattribute__(self, item)
#
#
#     def __setattr__(self, key, value):
#         if key in self.__dict__:
#             raise AttributeError('Изменение значения атрибута невозможно')
#         else:
#             object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         raise AttributeError('Удаление атрибута невозможно')




# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.attrs_num = len(kwargs) + 1
#         for key, value in kwargs.items():
#             object.__setattr__(self, key, value)
#
#     def __setattr__(self, key, value):
#         if hasattr(self, 'attrs_num'):
#             self.attrs_num += 1
#         object.__setattr__(self, key, value)
#
#
#     def __delattr__(self, item):
#         if hasattr(self, 'attrs_num'):
#             self.attrs_num -= 1
#         object.__delattr__(self, item)
#
#
# music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')
#
# print(music_group.attrs_num)
# del music_group.genre
# print(music_group.attrs_num)