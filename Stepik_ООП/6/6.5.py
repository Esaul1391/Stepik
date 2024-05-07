from time import perf_counter


class AdvancedTimer:
    def __init__(self, last_run=None, min=None, max=None):
        self.last_run = last_run
        self.runs = []
        self.max = max
        self.min = min

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = perf_counter() - self.start
        self.last_run = self.elapsed
        self.runs.append(self.elapsed)
        if self.min == None:
            self.min = self.elapsed
            self.max = self.elapsed
        if self.elapsed > self.max:
            self.max = self.elapsed
        if self.elapsed < self.min:
            self.min = self.elapsed


from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)
print(round(timer.last_run, 1))

with timer:
    sleep(0.7)
print(round(timer.last_run, 1))

with timer:
    sleep(1)
print(round(timer.last_run, 1))


# class Reloopable:
#     def __init__(self, file):
#         self.file = file
#
#     def __enter__(self):
#         self.obj = open(self.file, mode='r', encoding='utf-8', newline='\n')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.obj:
#             self.obj.close()



# class ReadableTextFile:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __enter__(self):
#         self.file = open(self.filename, mode='r', encoding='utf-8')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         line = self.file.readline()
#         if line:
#             return line.rstrip('\n')
#         else:
#             raise StopIteration
#
# with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
#     print('Только посмотрите!', file=file)
#     print('Как величаво она парит в воздухе', file=file)
#     print('Как орел', file=file)
#     print('На воздушном шаре', file=file)
#
# with ReadableTextFile('glados_quotes.txt') as file:
#     for line in file:
#         print(line)



# class Closer:
#     def __init__(self, obj):
#         self.obj = obj
#         self.closed = False
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             self.obj.close()
#             self.closed = True
#         except AttributeError:
#             print('Незакрываемый объект')
#             self.closed = False
#
# output = open('output.txt', 'w', encoding='utf-8')
#
# with Closer(output) as file:
#     print(file.closed)
#
# print(file.closed)



# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print(f'Приветствую, {self.name}!')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'До встречи, {self.name}!')




# class SuppressAll:
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             pass
#         return True

