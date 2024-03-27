# from enum import Enum
#
# class TrafficLights(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3
#
#
# print(TrafficLights.__repr__)





# class Shape:
#     __slots__ = ('name', 'color', 'area')
#
#     def __init__(self, name, color, area):
#         self.name = name
#         self.color = color
#         self.area = area
#
#     def __str__(self):
#         return f'{self.color} {self.name} ({self.area})'
#
#     def __eq__(self, other):
#         if not isinstance(other, Shape):
#             return NotImplemented
#         return self.area == other.area
#
#     def __ne__(self, other):
#         if not isinstance(other, Shape):
#             return NotImplemented
#         return self.area != other.area
#
#     def __gt__(self, other):
#         if not isinstance(other, Shape):
#             return NotImplemented
#         return self.area > other.area
#
#     def __lt__(self, other):
#         if not isinstance(other, Shape):
#             return NotImplemented
#         return self.area < other.area
#
#     def __ge__(self, other):
#         if not isinstance(other, Shape):
#             return NotImplemented
#         return self.area >= other.area
#
#     def __le__(self, other):
#         if not isinstance(other, Shape):
#             return NotImplemented
#         return self.area <= other.area