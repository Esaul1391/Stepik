import functools


class ignore_exception:
    def __init__(self, *args, **kwargs):
        self.ex = list(args) + list(kwargs.values())
        print()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                print(f'Исключение {e} обработано')
        return wrapper


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x


func(0)



# import functools
#
#
# class exception_decorator:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         try:
#             res = self.func(*args, **kwargs)
#             return (res, None)
#         except Exception as e:
#             return (None, type(e))




# import functools
#
#
# class returns:
#     def __init__(self, datetype):
#         self.datetype = datetype
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if not isinstance(result, self.datetype):
#                 raise TypeError
#             return result
#         return wrapper


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




