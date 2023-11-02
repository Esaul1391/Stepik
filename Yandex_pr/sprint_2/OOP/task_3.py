# class User:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def show(self):
#         print(f'{self.name} ({self.phone})')
#
#
# # объявляем класс Friend, дочерний по отношению к классу User
# class Friend(User):
#     def show(self):
#         print(f'Имя: {self.name} || Телефон: {self.phone}')
#
# father = User('Дюма-отец', '+33 3 23 96 23 30')
# son = Friend('Дюма-сын', '+33 3 23 96 23 30')
#
#
# father.show()
# son.show()


# class User:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def show(self):
#         print(f'{self.name} ({self.phone})')
#
#
# # наследуем класс Friend от User
# class Friend(User):
#     # Пишем конструктор класса-наследника,
#     # чтобы он принимал все нужные параметры
#     def __init__(self, name, phone, address):
#         # наследуем функциональность конструктора из класса-родителя
#         super().__init__(name, phone)
#         # добавляем новую функциональность: свойство address
#         self.address = address
#
#     # полностью переопределяем родительский метод show()
#     def show(self):
#         print(f'Имя: {self.name} || '
#               f'Телефон: {self.phone} || '
#               f'Адрес: {self.address}')
#
#
# Yar = Friend('Yar', '12334', 'Moskov')
# Yar.show()


class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')


class Friend(User):
    def show(self):
        print(f'Name: {self.name} || phone: {self.phone}')


user = User("Viktor", '123')

friend = Friend('Viktor', '123')

user.show()
friend.show()
