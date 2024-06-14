
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value







# class LineTo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class PathLines:
#     def __init__(self, *args):
#         self.coords = list((LineTo(0, 0), ) + args)
#
#
#     def get_path(self):
#         return self.coords[1:]
#
#     def get_length(self):
#         g = ((self.coords[i - 1], self.cords[i]) for i in range(1, len(self.coords)))
#         return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))
#
#     def add_line(self, line):
#         self.coords.append(line)
# class WindowDlg:
#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__width = self.__height = None
#         self.width = width
#         self.height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, num):
#         if self.check(num):
#             if self.__width:
#                 self.show()
#             self.__width = num
#
#     @property
#     def height(self):
#         return self.__height
#
#     @width.setter
#     def height(self, num):
#         if self.check(num):
#             if self.__height:
#                 self.show()
#             self.__height = num
#
#     def show(self):
#         print(f'{self.__title}: {self.__width}, {self.__height}')
#
#     @classmethod
#     def check(cls, value):
#         if isinstance(value, int) and 0 <= value < 1000:
#             return value

# class Car:
#     def __init__(self):
#         self.__model = None
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, m):
#         if self.check(m):
#             self.__model = m
#
#     @classmethod
#     def check(cls, n):
#         if isinstance(n, str) and 2 <= len(n) <100:
#             return n
