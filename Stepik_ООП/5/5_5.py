class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        return f'{self.hours}:{self.minutes}'

    def __add__(self, other):
        return Time(self.hours + other, self.hours + other)

    def __iadd__(self, other):
        self.hours += other
        self.minutes += other
        return self
    
time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)



# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented
#
#
#     def __radd__(self, other):
#         return self.__add__(other)
#




# class FoodInfo:
#     def __init__(self, proteins, fats, carbohydrates):
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates
#
#     def __repr__(self):
#         return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"
#
#     def __add__(self, other):
#         if isinstance(other, FoodInfo):
#             return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
#         return NotImplemented
#
#     def __mul__(self, n):
#         return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)
#
#     def __truediv__(self, n):
#         return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)
#
#     def __floordiv__(self, n):
#         return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)


