class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                setattr(self, key, abs(value))
            else:
                setattr(self, key, value)

point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)

# class DefaultObject:
#     def __init__(self, default=None, **kwargs):
#         self._default = default
#         self._attributes = kwargs
#
#     def __getattr__(self, attr):
#         return self._attributes.get(attr, self._default)
#
#
# god = DefaultObject(name='Kratos', mythology='greek')
# print('name' in god.__dict__)
# print('mythology' in god.__dict__)

# class Ord:
#     def __getattribute__(self, item):
#         res = str(ord(item))
#         return res
#
#
# obj = Ord()
#
# print(obj.a)
# print(obj.b)





# class Logger:
#     def __setattr__(self, key, value):
#         print(f'Изменение значения атрибута {key} на {value}')
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         print(f'Удаление атрибута {item}')
#         del self.__dict__[item]



# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __getattribute__(self, name):
#         if name == 'total':
#             return self.price * self.quantity
#         elif name == 'name':
#             return object.__getattribute__(self, name.title())
#         return object.__getattribute__(self, name)
#
#
# course = Item('pygen', 3900, 2)
#
# print(course.name)
# print(course.price)
# print(course.quantity)
# print(course.total)