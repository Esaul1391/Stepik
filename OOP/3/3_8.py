class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append(((x, y), speed))

    def __check_index(self, indx):
        if not isinstance(indx, int) or (-self.__total_attrs <= indx < self.__total_attrs):
            raise IndexError('неверный индекс поля')




# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         self.__total_attrs = len(kwargs)
#         self.__attrs = tuple(self.__dict__.keys())
#         # for k, v in kwargs.items():
#         #     self.k = v
#
#     def __check_index(self, indx):
#         if not isinstance(indx, int) or (-self.__total_attrs <= indx < self.__total_attrs):
#             raise IndexError('неверный индекс поля')
#
#     def __getitem__(self, item):
#         self.__check_index(item)
#         return getattr(self, self.__attrs[item])
#
#     def __setitem__(self, key, value):
#         self.__check_index(key)
#         setattr(self, self.__attrs[key], value)
