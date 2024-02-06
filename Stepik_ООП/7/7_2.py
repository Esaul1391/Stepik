class Summator:
    def __init__(self, m=1):
        self.m = m

    def total(self, n):
        return sum(map(lambda x: x ** self.m, range(1, n + 1)))


class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)


class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)


class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(m)

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
