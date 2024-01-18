class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return (f'Vector({self.x}, {self.y})')

    def __str__(self):
        return f'({self.x}, {self.y})'




# class Money:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __str__(self):
#         return f'{self.amount} руб.'
#
#
#     def __pos__(self):
#         return Money(abs(self.amount))
#
#     def __neg__(self):
#         return Money(-self.amount)
#
# money = Money(100)
#
# print(money)
# print(+money)
# print(-money)




# class ReversibleString:
#     def __init__(self, string):
#         self.string = string
#
#
#     def __str__(self):
#         return self.string
#
#     def __neg__(self):
#         return ReversibleString(self.string[::-1])
#
#
# string = ReversibleString('python')
#
# print(string)
# print(-string)