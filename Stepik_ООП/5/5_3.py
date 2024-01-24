from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.year, self.month) < other
        return NotImplemented

# from functools import total_ordering
#
# @total_ordering
# class Word:
#     def __init__(self, word):
#         self.word = word
#
#     def __repr__(self):
#         return f"Word('{self.word}')"
#
#     def __str__(self):
#         return f"{self.word.capitalize()}"
#
#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) == len(other.word)
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) < len(other.word)
#         return NotImplemented




# from functools import total_ordering
#
#
# @total_ordering
# class ElectricCar:
#     def __init__(self, power_reserve):
#         self.power_reserve = power_reserve
#
#     def __repr__(self):
#         return f'ElectricCar({self.power_reserve})'
#
#     def __eq__(self, other):
#         return self.power_reserve == other.power_reserve
#
#     def __lt__(self, other):
#         return self.power_reserve < other.power_reserve
#
#
# cars = [ElectricCar(330), ElectricCar(400), ElectricCar(290)]
#
# print(min(cars))
# print(max(cars))
# print(sorted(cars))