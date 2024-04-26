class Closer:
    def __init__(self, obj):
        self.obj = obj
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
            self.closed = True
        except AttributeError:
            print('Незакрываемый объект')
            self.closed = False

output = open('output.txt', 'w', encoding='utf-8')

with Closer(output) as file:
    print(file.closed)

print(file.closed)



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

