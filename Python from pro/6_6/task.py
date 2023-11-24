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
new_data = OrderedDict()

for rule in (True, False) * (len(data)//2) :
    key, value = data.popitem(last=rule)
    new_data[key] = value

print(new_data)