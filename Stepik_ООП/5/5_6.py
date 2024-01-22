class RaiseTo:
    def __init__(self, degree):
        self.degree = degree


    def __call__(self, x):
        return pow(x, self.degree)


raise_to_two = RaiseTo(2)

print(raise_to_two(2))
print(raise_to_two(3))
print(raise_to_two(4))










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