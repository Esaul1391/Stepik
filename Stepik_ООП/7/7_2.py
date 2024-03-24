<<<<<<< HEAD
class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.month}-{self.day}-{self.year}'

    def iso_format(self):
        return f"{self.year}-{self.month}-{self.day}"









# res = {}
# for num in numbers:
#     if num not in res:
#         res[num] = 1
#     else:
#         res[num] += 1
#
# item = info.get('key', default=None)  возвращ значение по умолчанию не меняя словаря
# info1.update(info2)   info1 |= info2
# dict.setdefault(key, default=None)  если ключ отсутсвует вставляет значение изменяя словарь
# def info['job']
# job = info.pop('job', None)
# job = info.popitem()  удалит последний элемент словаря
# description = {1 : 'ONE', 2 : 'TWO', 3 : 'TREE'}
# print(description.get(num, 'Unknown'))
#








# s = input().split(' ')
# d = {}
# sp = []
# for i in s:
#     d[i] = d.setdefault(i, 0) + 1
#     sp.append(d[i])
# print(*sp)


# def build_query_string(params):
#     # Сортируем ключи словаря
#     sorted_keys = sorted(params.keys())
#
#     # Формируем список строк вида "ключ=значение"
#     query_list = [f"{key}={params[key]}" for key in sorted_keys]
#
#     # Объединяем список строк с помощью символа "&"
#     query_string = "&".join(query_list)
#
#     return query_string
#
# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

#     def __init__(self, m=1):
#         self.m = m
#
#     def total(self, n):
#         return sum(map(lambda x: x ** self.m, range(1, n + 1)))
#
#
# class SquareSummator(Summator):
#     def __init__(self):
#         super().__init__(2)
#
#
# class QubeSummator(Summator):
#     def __init__(self):
#         super().__init__(3)
#
#
# class CustomSummator(Summator):
#     def __init__(self, m):
#         super().__init__(m)

# class Counter:
#     def __init__(self, start=0):
#         self.start = start
#         self.value = start
#
#     def inc(self, num=1):
#         self.value += num
#
#     def dec(self, num=1):
#         self.value = max(0, self.value - num)
#
#
# class DoubledCounter(Counter):
#     def inc(self, num=1):
#         super().inc(num * 2)
#
#     def dec(self, num=2):
#         super().dec(num * 2)
#
#
# counter = DoubledCounter(20)
#
# print(counter.value)
# counter.inc()
# counter.inc(5)
# print(counter.value)
# counter.dec()
# counter.dec(10)
# print(counter.value)
# counter.dec(10)
# print(counter.value)
=======
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.c = c
        self.b = b

    def perimeter(self):
        return sum(self.a, self.b, self.c)


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.side = side



# class WeatherWarning:
#     def rain(self):
#         print('Ожидаются сильные дожди и ливни с грозой')
#
#     def snow(self):
#         print('Ожидается снег и усиление ветра')
#
#     def low_temperature(self):
#         print('Ожидается сильное понижение температуры')
#
#
# class WeatherWarningWithDate(WeatherWarning):
#     def rain(self, data):
#         print(f'{data.strftime("%d.%m.%Y")}\nОжидаются сильные дожди и ливни с грозой')
#
#     def snow(self, data):
#         print(f'{data.strftime("%d.%m.%Y")}\nОжидается снег и усиление ветра')
#
#     def low_temperature(self, data):
#         print(f'{data.strftime("%d.%m.%Y")}\nОжидается сильное понижение температуры')
#
# from datetime import date
#
# weatherwarning = WeatherWarningWithDate()
# dt = date(2022, 12, 12)
#
# weatherwarning.rain(dt)
# weatherwarning.snow(dt)
# weatherwarning.low_temperature(dt)

# class BasicPlan:
#     def __init__(self):
#         self.can_stream = True
#         self.can_download = True
#         self.has_SD = True
#         self.has_HD = False
#         self.has_UHD = False
#         self.num_of_devices = 1
#         self.price = "8.99$"
#
# class SilverPlan(BasicPlan):
#     def __init__(self):
#         self.can_stream = True
#         self.can_download = True
#         self.has_SD = True
#         self.has_HD = True
#         self.has_UHD = True
#         self.num_of_devices = 4
#         self.price = "15.99$"
#
#
# print(SilverPlan.can_stream)
# print(SilverPlan.can_download)
# print(SilverPlan.has_SD)
# print(SilverPlan.has_HD)
# print(SilverPlan.has_UHD)
# print(SilverPlan.num_of_devices)
# print(SilverPlan.price)
>>>>>>> 582a0dd (1)
