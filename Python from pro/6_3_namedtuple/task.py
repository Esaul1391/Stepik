# from collections import namedtuple
#
# Tree = namedtuple('Tree', 'name,colors,height')
#
# cruenta = Tree(height=2, name='Cruenta', colors=('red', 'green'))
#
# print(cruenta)


# from collections import namedtuple
#
# headers = ('_name', 'surname', 'age', 'class')
#
# Student = namedtuple('Student', headers, rename=True)
#
# spidey = Student('Peter', 'Parker', 15, 10)
#
# print(spidey)

#
# from collections import namedtuple
#
# Integer = namedtuple('Integer', ['value', 'even', 'divisors'])
#
# number = Integer(16, True, [1, 2, 4])
#
# number.divisors.extend([8, 16])
#
# print(len(number.divisors))


# from collections import namedtuple
#
# Resolution = namedtuple('Resolution', ['horizontal', 'vertical'])
#
# full_hd = Resolution(1920, 1070)
#
# full_hd._replace(vertical=1080)
#
# print(full_hd.vertical)



# from collections import namedtuple
#
# PcHardware = namedtuple('PcHardware', 'cpu,gpu,motherboard,ram', defaults=[None, None])
#
# print(PcHardware)


# from collections import namedtuple
#
# App = namedtuple('App', ['name', 'apptype', 'size'])
#
# app = App._make('Discord messenger 200'.split())
#
# print(app)


# from collections import namedtuple
#
# Device = namedtuple('Device', ['devicetype', 'model'])
#
# device1 = Device(**{'devicetype': 'keyboard', 'model': 'Logitech G213'})
# device2 = Device(*{'devicetype': 'keyboard', 'model': 'Logitech G213'})
#
# print(device1, sep=', ')
# print(device2, sep=', ')

# from collections import namedtuple
#
# Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])
# print(Fruit)



# from collections import namedtuple
#
# Game = namedtuple('Game', 'name developer publisher')
#
# ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])


# from collections import namedtuple
# import pickle
#
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])\
#
# with open('data.pkl', 'rb') as file:
#     animal_list = pickle.load(file)
#
# for animal in animal_list:
#     print(f'name: {animal.name}')
#     print(f'family: {animal.family}')
#     print(f'sex: {animal.sex}')
#     print(f'color: {animal.color}')
#     print()  # Пустая строка м


# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
#
#
# # Функция для определения порядка сортировки
# def sort_key(user):
#     # Порядок подписок от дорогой к дешевой
#     plans_order = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 'Basic': 4}
#
#     return (plans_order[user.plan], user.email)
#
#
# # Сортируем пользователей
# sorted_users = sorted(users, key=sort_key)
#
# # Выводим данные о пользователях
# for user in sorted_users:
#     print(f'{user.name} {user.surname}')
#     print(f'  Email: {user.email}')
#     print(f'  Plan: {user.plan}\n')


import csv
from datetime import datetime
from collections import namedtuple

# Определяем именованный кортеж для представления данных о встречах
Meeting = namedtuple('Meeting', ['surname', 'name', 'meeting_date', 'meeting_time'])

meetings = []

# Открываем CSV файл с указанием кодировки UTF-8
with open('meetings.csv', 'r', encoding='utf-8') as file:
    csv_reader = list(csv.reader(file))

    # Пропуск заголовка
    # next(csv_reader)
    csv_reader = csv_reader[1:]
    csv_reader.sort(key=lambda x: (x[2], x[3]))
    print(csv_reader)
    for row in csv_reader:
        # Преобразование даты и времени в формат datetime
        print(row)
#         date = datetime.strptime(row[2], '%d.%m.%Y')
#         time = datetime.strptime(row[3], '%H:%M')
#
#         # Создаем экземпляр именованного кортежа Meeting
#         meeting = Meeting(row[0], row[1], date, time)
#         meetings.append(meeting)
#
# # Сортируем данные по дате и времени
# meetings.sort(key=lambda x: (x.meeting_date, x.meeting_time))
#
# # Выводим фамилии и имена друзей в отсортированном порядке
# for meeting in meetings:
#     print(f'{meeting.surname} {meeting.name}')
