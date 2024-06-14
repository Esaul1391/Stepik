
class Factory:
    def build_sequence(self):
        sp = []
        return sp

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
print()


















# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self, *args, **kwargs):
#         return Point(self.x, self.y)
#
#
# pt = Point(1, 3)
# pt_clone = pt.clone(3, 4)

# TYPE_OS = 1  # 1 - Windows; 2 - Linux
#
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         obj = None
#         if TYPE_OS == 1:
#             obj = super().__new__(DialogWindows)
#         else:
#             obj = super().__new__(DialogLinux)
#         return obj
#
#     def __init__(self, name):
#         self.name = name

# class SingletonFive:
#     _count_class = 0
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._count_class < 5:
#             cls._count_class += 1
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]
#
# print(objs[7].name)

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"
