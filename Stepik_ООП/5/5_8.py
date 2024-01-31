class Const:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)


    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')




# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.attrs_num = len(kwargs) + 1
#         for key, value in kwargs.items():
#             object.__setattr__(self, key, value)
#
#     def __setattr__(self, key, value):
#         if hasattr(self, 'attrs_num'):
#             self.attrs_num += 1
#         object.__setattr__(self, key, value)
#
#
#     def __delattr__(self, item):
#         if hasattr(self, 'attrs_num'):
#             self.attrs_num -= 1
#         object.__delattr__(self, item)
#
#
# music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')
#
# print(music_group.attrs_num)
# del music_group.genre
# print(music_group.attrs_num)