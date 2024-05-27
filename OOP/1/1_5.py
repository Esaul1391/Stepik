from random import randint

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False



class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)]]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1
        index = (-1, -1), (-1, 0), (-1, 1), (-1, -1), (-1, 0), (-1, 1), (-1, -1), (-1, 0)
        for x in range(self._n):
            for y in range(self._n):
                mines = sum(())


# import sys
#
#
# class ListObject:
#     def __init__(self, data):
#         self.next_obj = None
#         self.data = data
#
#     def link(self, obj):
#         self.next_obj = obj
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     obj_new = ListObject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new




# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, index):
#         del self.goods[index]
#
#     def get_list(self):
#         return list(map(lambda x: f"{x.name}: {x.price}", self.goods))
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
#
# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1 = Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
#
# cart.add(tv1)
# cart.add(tv2)
# cart.add(table)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, *mems):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mems[:self.total_mem_slots]
#
#     def get_config(self):
#         return [f'Материнская плата: {self.name}',
#                 f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slots}',
#                 'Память: ' + '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))
#                 ]


# mb = MotherBoard('Asus', CPU('intel i7', 3500), Memory('Kingston', 4600), Memory('Kingston', 4600))
#
# print(mb.get_config())

# cpu = CPU('asus', 1333)
# mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
# mb = MotherBoard('Asus', cpu, [mem1, mem2])
# print(mb.get_config())

# class Graph:
#     def __init__(self, data):
#         self.data = list(data)
#         self.is_show = True
#
#     def set_data(self, data):
#         self.data = list(data)
#
#
#     def _get_str_date(self):
#         return ' '.join(map(str, self.data))
#
#     def show_table(self):
#         if self.is_show:
#             print(*self.data)
#         else:
#             print("Отображение данных закрыто")
#
#     def show_graph(self):
#         if self.is_show:
#             print(f"Графическое отображение данных: {self._get_str_date()}")
#         else:
#             print("Отображение данных закрыто")
#
#     def show_bar(self):
#         if self.is_show:
#             print(f"Столбчатая диаграмма: {self._get_str_date()}")
#         else:
#             print("Отображение данных закрыто")
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
# data_graph = [1, 2, 3, 4]
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
#             return 1
#         if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
#             return 1
#         a, b, c = self.a, self.b, self.c
#         if a >= b + c or b >= a + c or c >= a + b:
#             return 2
#         return 3
#
#
# a, b, c = map(int, input().split())
#
# tr = TriangleChecker(a, b, c)

# from random import randint
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4) for _ in range(217)]
# for obj in elements:
#     if isinstance(obj, Line):
#         obj.sp = obj.ep = 0, 0
#
# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# count = 1
# points = []
# while len(points) < 1001:
#     if len(points) == 1:
#         points.append(Point(count, count, color='yellow'))
#     else:
#         points.append(Point(count, count))
#     count += 2
#
#
# class Money:
#     def __init__(self, money):
#         self.money = money
