import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))

    def select(self, a, b):
        if b > len(self.lst_data):
            b = len(self.lst_data)
        return self.lst_data[a:b+1]


db = DataBase()
db.insert(lst_in)






# import sys
#
#
# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#
#         for i, key in enumerate(fields):
#             setattr(self, key, lst_values[i])
#
#         return True
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
# sr = StreamReader()
# data, result = sr.readlines()



# class Graph:
#
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         LIMIT_Y = [0, 10]
#         print(' '.join(map(str, filter(lambda x: LIMIT_Y[0] <= x <= LIMIT_Y[1], self.data))))
#
# graph_1 = Graph()
#
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()








# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open('filemedia1')
# media2.open('filemedia2')
#
# media1.play()
# # media2.play()