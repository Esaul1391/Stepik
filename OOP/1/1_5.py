class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not isinstance(self.a, (int, float)) or self.a == 0:
            return 1
        if not isinstance(self.b, (int, float)) or self.b == 0:
            return 1
        if not isinstance(self.c, (int, float)) or self.c == 0:
            return 1
        if sum(self.a, self.b, self.c) != 180:
            return 2
        return 3


a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)

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
