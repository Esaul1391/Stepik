# import functools
# def add_smiley_face(face='>.<'):
#     def smiley_face_decorator(func):
#         def wrapper():
#             return func() + ' ' + face
#         return wrapper
#     return smiley_face_decorator
#
# @add_smiley_face
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())

def add_smiley_face(face):
    def smiley_face_decorator(func):
        def wrapper():
            return func() + ' ' + face
        return wrapper
    return smiley_face_decorator

@add_smiley_face('^~^')
def beegeek():
    return 'beegeek'

print(beegeek())

# import functools
# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
#         res = func(*args, **kwargs)
#         print(f"TRACE: возвращаемое значение {func.__name__}(): {res}")
#         return res
#     return wrapper
#





# def sandwich(func):
#     def wrapper(*args, **kwargs):
#         print("---- Верхний ломтик хлеба ----")
#         result = func(*args, **kwargs)
#         print("---- Нижний ломтик хлеба ----")
#         return result
#     # return wrapper
#
#
# @sandwich
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())

# def scream_decorator(func):
#     def wrapper(*args, **kwargs):
#         s_args = (str(i).upper()for i in args)
#         s_kwargs = {k: str(v).upper() for k,v in kwargs.items()}
#         res = func(*s_args, **s_kwargs)
#         return res
#     return wrapper


# def flip(func):
#     def wrapper(*args, **kwargs):
#         rev = reversed(args)
#         res = func(*rev, **kwargs)
#         return res
#     return wrapper
#
#
# @flip
# def div(x, y, show=False):
#     res = x / y
#     if show:
#         print(res)
#     return res
#
#
# div(2, 4, show=True)


# def optional_introduce(func):
#     def wrapper(*args, introduce=False, **kwargs):
#         if introduce == True:
#             print(func.__name__)
#         return func(*args)
#     return wrapper
# @optional_introduce
# def identity(x):
#     return x
#
#
# print(identity(20))