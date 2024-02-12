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
