import functools


class returns:
    def __init__(self, datetype):
        self.datetype = datetype


    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if any((
                    not all(isinstance(arg, (self.datetype)) for arg in args),
                    not all(isinstance(arg, (self.datetype)) for arg in kwargs.values())
            )):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper

@returns(int)
def add(a, b):
    return a + b

try:
    print(add('1', '2'))
except Exception as error:
    print(type(error))



# import functools
#
# class takes_numbers:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         for i in args:
#             if not isinstance(i, (int, float)):
#                 raise TypeError('Аргументы должны принадлежать типам int или float')
#         for i in kwargs.values():
#             if not isinstance(i, (int, float)):
#                 raise TypeError('Аргументы должны принадлежать типам int или float')
#         return self.func(*args, **kwargs)




