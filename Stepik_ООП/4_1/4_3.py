class Wordplay:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args):
        return [word for word in self.words if set(word).issubset(set(args))]

    def avoid(self, *args):
        return [word for word in self.words if not set(word).issubset(set(args))]









# class Postman:
#     def __init__(self):
#         self.delivery_data = []
#
#     def add_delivery(self, street, house, apartment):
#         self.delivery_data.append((street, house, apartment))
#
#     def get_houses_for_street(self, street_name):
#         res = [house for street, house, apartment in self.delivery_data if street == street_name]
#         return sorted(set(res), key=lambda d: res.index(d))                                                         # интересный способ убрать дубликаты в списке
#
#     def get_flats_for_house(self, street_name, house_num):
#         res = [apartment for street, house, apartment in self.delivery_data if street == street_name and house == house_num]
#         return sorted(set(res), key=lambda d: res.index(d))








# class Todo:
#     def __init__(self):
#         self.things = []
#
#     def add(self, name, prior):
#         self.things.append((name, prior))
#
#     def get_by_priority(self, number):
#         return [task[0] for task in self.things if task[1] == number]
#
#     def get_low_priority(self):
#         if not self.things:
#             return []
#         min_priority = min(self.things, key=lambda x: x[1])[1]
#         return [task[0] for task in self.things if task[1] == min_priority]
#
#     def get_high_priority(self):
#         if not self.things:
#             return []
#         max_priority = max(self.things, key=lambda x: x[1])[1]
#         return [task[0] for task in self.things if task[1] == max_priority]
#
# todo = Todo()
#
# print(todo.things)
# print(todo.get_by_priority(1))
# print(todo.get_low_priority())
# print(todo.get_high_priority())
#
#
#
#
# class Todo:
#     def __init__(self):
#         self.things = []
#
#     def add(self, name, priority):
#         self.things.append((name, priority))
#
#     def get_by_priority(self, n):
#         return [name for name, priority in self.things if priority == n]
#
#     def get_low_priority(self):
#         min_priority = min(self.things, key=lambda x: x[1], default=(None,))[1]
#         return [name for name, priority in self.things if priority == min_priority]
#
#     def get_high_priority(self):
#         max_priority = max(self.things, key=lambda x: x[1], default=(None,))[1]
#         return [name for name, priority in self.things if priority == max_priority]


# class TextHandler:
#     def __init__(self):
#         self.words = []
#
#     def add_words(self, text):
#         words = text.split()
#         self.words.extend(words)
#
#     def get_shortest_words(self):
#         if not self.words:
#             return []
#         min_length = min(len(word) for word in self.words)
#         return [word for word in self.words if len(word) == min_length]
#
#     def get_longest_words(self):
#         if not self.words:
#             return []
#         max_length = max(len(word) for word in self.words)
#         return [word for word in self.words if len(word) == max_length]





# class Numbers:
#     def __init__(self):
#         self.sp = []
#
#     def add_number(self, i):
#         if isinstance(i, int):
#             self.sp.append(i)
#
#     def get_even(self):
#         res = filter(lambda x: x % 2 == 0, self.sp)
#         return list(res)
#
#     def get_odd(self):
#         res = filter(lambda x: x % 2 == 1, self.sp)
#         return list(res)


# import math
#
# class Vector:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def abs(self):
#         return math.sqrt(pow(self.x, 2) + pow(self.y, 2))


# class Bee:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def move_up(self, n):
#         self.y += n
#
#     def move_down(self, n):
#         self.y -= n
#
#     def move_right(self, n):
#         self.x += n
#
#     def move_left(self, n):
#         self.x -= n
#
#
# bee = Bee()
#
# bee.move_right(2)
# bee.move_right(2)
# bee.move_up(3)
# bee.move_left(1)
# bee.move_down(1)
#
# print(bee.x, bee.y)

# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2
#         self.area = pi * radius ** 2
#
#
# circle = Circle(5)
#
# print(circle.area)

# class House:
#     def __init__(self, color, rooms):
#         self.color = color
#         self.rooms = rooms
#
#     def paint(self, new_color):
#         self.color = new_color
#
#     def add_rooms(self, n):
#         self.rooms += n


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.friends = 0
#
#     def add_friends(self, n):
#         self.friends += n

# user = User('Timur')
#
# user.add_friends(2)
# user.add_friends(2)
# user.add_friends(3)
#
# print(user.friends)


# class Gun:
#     def __init__(self):
#         self.counter = 0
#
#     def shoot(self):
#         self.counter += 1
#         print('pif' if self.counter % 2 == 1 else 'paf')
#
#     def shots_count(self):
#         return self.counter
#
#     def shots_reset(self):
#         self.counter = 0
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# print(gun.shots_count())
# gun.shots_reset()
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
