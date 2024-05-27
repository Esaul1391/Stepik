class SingletonFive:
    _count_class = 0
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._count_class < 5:
            cls._count_class += 1
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]

print(objs[7].name)

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"
