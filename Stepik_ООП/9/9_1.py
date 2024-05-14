class Anything:
    # def __init__(self, value):
    #     self.value = value

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __le__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return True


def anything():
    a = Anything()
    return a

import math, re

print(anything() != [])
print(anything() < 'World')
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)