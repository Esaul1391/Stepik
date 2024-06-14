





# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return (self.__x1, self.__y1, self.__x2, self.__y2)
#
#     def draw(self):
#         print(self.__x1, self.__y1, self.__x2, self.__y2)




# class Book:
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price




# class Money:
#     def __init__(self, mn):
#         self.__money = 0
#         if self.__check_money(mn):
#             self.__money = mn
#
#     @classmethod
#     def __check_money(cls, money):
#         return isinstance(money, int) and money >= 0
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.__money += mn.get_money()

#
# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120
#
# print(m2)



# class Clock:
#     def __init__(self, time=0):
#         self.__time = time
#
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     @classmethod
#     def __check_time(cls, tm):
#         return isinstance(tm, int) and 0 <= tm < 100000
#
# clock = Clock(4530)