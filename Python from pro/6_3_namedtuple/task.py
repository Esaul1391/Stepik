# from collections import namedtuple
#
# Tree = namedtuple('Tree', 'name,colors,height')
#
# cruenta = Tree(height=2, name='Cruenta', colors=('red', 'green'))
#
# print(cruenta)


# from collections import namedtuple
#
# headers = ('_name', 'surname', 'age', 'class')
#
# Student = namedtuple('Student', headers, rename=True)
#
# spidey = Student('Peter', 'Parker', 15, 10)
#
# print(spidey)

#
# from collections import namedtuple
#
# Integer = namedtuple('Integer', ['value', 'even', 'divisors'])
#
# number = Integer(16, True, [1, 2, 4])
#
# number.divisors.extend([8, 16])
#
# print(len(number.divisors))


# from collections import namedtuple
#
# Resolution = namedtuple('Resolution', ['horizontal', 'vertical'])
#
# full_hd = Resolution(1920, 1070)
#
# full_hd._replace(vertical=1080)
#
# print(full_hd.vertical)



# from collections import namedtuple
#
# PcHardware = namedtuple('PcHardware', 'cpu,gpu,motherboard,ram', defaults=[None, None])
#
# print(PcHardware)


# from collections import namedtuple
#
# App = namedtuple('App', ['name', 'apptype', 'size'])
#
# app = App._make('Discord messenger 200'.split())
#
# print(app)


# from collections import namedtuple
#
# Device = namedtuple('Device', ['devicetype', 'model'])
#
# device1 = Device(**{'devicetype': 'keyboard', 'model': 'Logitech G213'})
# device2 = Device(*{'devicetype': 'keyboard', 'model': 'Logitech G213'})
#
# print(device1, sep=', ')
# print(device2, sep=', ')

# from collections import namedtuple
#
# Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])
# print(Fruit)



# from collections import namedtuple
#
# Game = namedtuple('Game', 'name developer publisher')
#
# ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])


