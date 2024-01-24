class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return 9/5 * self.temperature + 32

    @staticmethod
    def from_fahrenheit(cls, fahrenheit_temperature):
        celsius_temperature = 5/9 * (fahrenheit_temperature - 32)
        return cls(celsius_temperature)

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)





# class CountCalls:
#     def __init__(self, func):
#         self.func = func
#         self.calls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         return self.func(*args, **kwargs)





# from datetime import date
#
# class DateFormatter:
#     def __init__(self, country_code):
#         self.country_code = country_code
#
#     def __call__(self, d):
#         if self.country_code == 'ru':
#             return d.strftime('%d.%m.%Y')
#         elif self.country_code == 'us':
#             return d.strftime('%m-%d-%Y')
#         elif self.country_code == 'ca':
#             return d.strftime('%Y-%m-%d')
#         elif self.country_code == 'br':
#             return d.strftime('%d/%m/%Y')
#         elif self.country_code == 'fr':
#             return d.strftime('%d.%m.%Y')
#         elif self.country_code == 'pt':
#             return d.strftime('%d-%m-%Y')
#         else:
#             raise ValueError("Invalid country code")



# class Filter:
#     def __init__(self, predicate):
#         if predicate is not None:
#             self.predicate = predicate
#         else:
#             self.predicate = bool
#
#
#     def __call__(self, iterable):
#         return list(filter(self.predicate, iterable))
#
# leave_even = Filter(lambda x: x % 2 == 0)
# numbers = [1, 2, 3, 4, 5, 6]
#
# print(leave_even(numbers))

# class Strip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         return string.strip(self.chars)
#
# strip = Strip('.,+-')
#
# print(strip('     --++beegeek++--'))
# print(strip('-bee...geek-'))
# print(strip('-+,.b-e-e-g-e-e-k-+,.'))

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return self.a * x**2 + self.b * x + self.c
#


# import random
#
# class Dice:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def __call__(self):
#         return random.randint(1, self.sides) if self.sides > 1 else 1
#
# kingdice = Dice(1)
#
# print(kingdice() == 1)
# print(kingdice() in [1, 2])
# print(kingdice() in [3, 4])
# print(kingdice() in [7, 8, 9, 10])




# class RaiseTo:
#     def __init__(self, degree):
#         self.degree = degree
#
#
#     def __call__(self, x):
#         return pow(x, self.degree)
#
#
# raise_to_two = RaiseTo(2)
#
# print(raise_to_two(2))
# print(raise_to_two(3))
# print(raise_to_two(4))










# class Calculator:
#     def __call__(self, a, b, operation):
#             if int(b) == 0 and operation == '/':
#                 return 'Деление на ноль невозможно'
#             return eval(f'{a}{operation}{b}')
#
#
#
#
# calculator = Calculator()
#
# try:
#     print(calculator(10, 0, '/'))
# except ValueError as e:
#     print(e)