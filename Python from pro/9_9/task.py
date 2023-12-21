from functools import partial

beegeek = partial(print, sep=', ')

beegeek('beegeek', 'stepik', 'python', sep='-')

# from functools import partial
#
# beegeek = partial(print, 'bee', 'geek', end='!')
#
# print(beegeek.args)
# print(beegeek.keywords)
# from functools import partial
#
# beegeek = partial(print, 'beegeek', sep=', ')
#
# beegeek('stepik', 'python')

# from functools import partial
#
# beegeek = partial(print, 'beegeek')
#
# beegeek('stepik', 'python')
# from functools import partial, update_wrapper
#
# def add(a, b):
#     '''documentation'''
#     return a + b
#
# add_one = partial(add, 1)
# update_wrapper(add_one, add)
#
# print(add_one.__name__)
# print(add_one.__doc__)


# from functools import partial
#
# def add(a, b):
#     return a + b
#
# add_one = partial(add, 1)
#
# print(add_one.func.__name__)
# print(add_one.func(2, 3))