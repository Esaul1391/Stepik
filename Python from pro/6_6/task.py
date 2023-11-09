# from collections import OrderedDict
#
# grades = OrderedDict(Timur=100, Arthur=84, Anri=94, Dima=98)
# new_grades = OrderedDict()
#
# for rule in (True, False, False, True):
#     name, grade = grades.popitem(last=rule)
#     new_grades[name] = grade
#
# print(*new_grades)



from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

# data_copy = data.copy()
# for i in data_copy:
#     data.move_to_end(i)
data = reversed(data.items())
print(*data)