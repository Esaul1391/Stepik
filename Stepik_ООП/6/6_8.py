


class Versioned:
    def __init__(self):
        self.all_attrs = []

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        raise AttributeError('Атрибут не найден')

    def get_version(self, instance, n):
        pass

    def set_version(self, instance, n):
        pass




# class TypeChecked:
#     def __init__(self, *attrs):
#         self.attrs = attrs
#
#     def __set_name__(self, owner, name):
#         self._name = name
#
#     def __get__(self, instance, owner):
#         if self._name in instance.__dict__:
#             return instance.__dict__[self._name]
#         raise AttributeError('Атрибут не найден')
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.attrs):
#             raise TypeError('Некорректное значение')
#         instance.__dict__[self._name] = value




# class MaxCallsException(Exception):
#     pass
#
# class LimitedTakes:
#     def __init__(self, times):
#         self.times = times
#         self.count = 0
#         self.value = None
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self.count >= self.times:
#             raise MaxCallsException("Превышено количество доступных обращений")
#         if self.value is None:
#             raise AttributeError('Атрибут не найден')
#         self.count += 1
#         return self.value
#
#     def __set__(self, obj, value):
#         self.value = value






# class NonNegativeInteger:
#     def __init__(self, attr, default=None):
#         self._attr = attr
#         self.default = default
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__ and self.default is None:
#             raise AttributeError('Атрибут не найден')
#         if self._attr not in obj.__dict__:
#             return self.default
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError('Некорректное значение')
#         obj.__dict__[self._attr] = value
#
#
# class Student:
#     score = NonNegativeInteger('score')
#
# print(Student.score.__class__)







# from keyword import kwlist
#
#
#
#
# class NonKeyword:
#     def __init__(self, name):
#         self._name = name
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._name not in obj.__dict__:
#             raise AttributeError('Атрибут не найден')
#         return obj.__dict__[self._name]
#
#     def __set__(self, obj, value):
#         if value in kwlist:
#             raise ValueError('Некорректное значение')
#         obj.__dict__[self._name] = value
#
#
# class Student:
#     name = NonKeyword('name')
#
# student = Student()
# student.name = 'Peter'
#
# try:
#     student.name = 'class'
# except ValueError as e:
#     print(e)






# class PositiveNumber:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         print('Вызов метода __get__()')
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         print('Вызов метода __set__()')
#         if type(value) in (int, float) and value > 0:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
# class Cat:
#     age = PositiveNumber()
#
#     def __init__(self, age):
#         self.__dict__['age'] = age
#
#
# cat = Cat(1)
#
# print(cat.age)






# class PositiveNumber:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         print('Вызов метода __get__()')
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         print('Вызов метода __set__()')
#         if type(value) in (int, float) and value > 0:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
# class Cat:
#     age = PositiveNumber()
#
#     def __init__(self, age):
#         self.age = age


# cat = Cat(1)
#
# print(cat.age)