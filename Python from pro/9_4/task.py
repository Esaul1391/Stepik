# def draw_triangle(size, color='black', fill=False):
#     pass
#
# print(draw_triangle.__defaults__)


# def bee():
#     return 'bee'
#
# def geek():
#     return 'geek'
#
# bee, geek = geek, bee
#
# print(bee())
# print(geek())


# methods = [str.upper, str.lower, str.title]
# text = 'heLLO wORld'
#
# text = methods[0](text)
# text = methods[1](text)
# text = methods[2](text)
#
# print(text)


# def ru_greeting(name):
#     print('Привет,', name)
#
#
# def en_greeting(name):
#     print('Hello,', name)
#
#
# greeting = {'ru': ru_greeting,
#             'en': en_greeting}
#
# greeting['ru']('Тимур')


# def add_name(name, names=[]):
#     names.append(name)
#
# add_name('Timur')
# add_name('Arthur')
# add_name('Dima')
#
# print(*add_name.__defaults__)

def numbers_sum(elems):
    if not elems:
        return 0
    return sum(filter(lambda x: isinstance(x, (int, float)), elems))

