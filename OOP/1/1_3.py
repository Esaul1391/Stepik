class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
if hasattr(p1.__dict__, 'job'):
    print(True)
else:
    print(False)

# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
#
# fig1 = Figure()
#
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'
#
# delattr(fig1, 'color')
# print(*fig1.__dict__.keys())


# class TravelBlog:
#     total_blogs = 0
#
#
# tb1 = TravelBlog()
#
# tb1.name = 'Франция'
# tb1.days = 6
#
# TravelBlog.total_blogs += 1
#
#
# tb2 = TravelBlog()
# tb2.name = 'Италия'
# tb2.days = 5
#
# TravelBlog.total_blogs += 1

# class Dictionary:
#     rus = 'Питон'
#     eng = 'Python'
#
# print(getattr(Dictionary, 'rus_word', False))


# class Car:
#     pass
#
#
# setattr(Car, 'model', 'Тайота')
# setattr(Car, 'color', 'Розовый')
# setattr(Car, 'number', 'П111УУ77')
#
# print(Car.__dict__['color'])


# class Goods:
#     title = "Мороженое"
#     weight = 154
#     tp = "Еда"
#     price = 1024
#
#
# Goods.price = 2048
# Goods.inflation = 100


# class Notes:
#     uid = 1005435
#     title = "Шутка"
#     author = "И.С. Бах"
#     pages = 2
#
# r = getattr(Notes, 'author')
# print(r)
