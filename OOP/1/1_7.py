class AppStore:
    """Объявите класс AppStore - интернет-магазин приложений для устройств
    под iOS. В этом классе должны быть реализованы следующие методы:
    """

    def __init__(self):
        self.store_app = {}

    def add_application(self, app):
        """добавление нового приложения app в магазин
        """
        self.store_app[id(app)] = app

    def remove_application(self, app):
        """удаление приложения app из магазина
        """
        self.store_app.pop(id(app))

    def block_application(self, app):
        """блокировка приложения app (устанавливает локальное
        свойство blocked объекта app в значение True)
        """
        obj = self.store_app.get(id(app), False)
        if not obj:
            return
        obj.blocked = True
        return True

    def total_apps(self):
        """возвращает общее число приложений в магазине
        """
        return len(self.store_app)


class Application:
    """Здесь Application - класс, описывающий добавляемое приложение
    с указанным именем. Каждый объект класса Application должен содержать
    локальные свойства:
    name - наименование приложения (строка);
    blocked - булево значение (True - приложение заблокировано;
    False - не заблокировано, изначально False).
    Как хранить список приложений в объектах класса AppStore решите сами.
    """

    def __init__(self, name):
        self.name = name
        self.blocked = False

# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
# class YouTube:
#     videos = []
#     @classmethod
#     def add_video(cls, video):
#         YouTube.videos.append(video)
#
#     @classmethod
#     def play(cls, video_index):
#         return YouTube.videos.index(video_index)
#
# v1 = Video()
# v2 = Video()
# v1.create("Python")
# v2.create("Python ООП")
# YouTube.add_video(v1.play())
# YouTube.add_video(v2.play())


# from string import ascii_lowercase, digits
#
# class CardCheck:
#     def check_card_number(number):
#         return all(map(lambda x: True if x.isdigit() or x == '-' else False, number))
#
#     def check_name(name):
#         CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#         return set(name) < set(CHARS_FOR_NAME)


# from string import ascii_lowercase, digits
#
#
# CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
# # здесь объявляйте классы TextInput и PasswordInput
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if type(name) != str or len(name) < 3 or len(name) > 50:
#             raise ValueError("некорректное поле name")
#         if set(name) < set(cls.CHARS_CORRECT):
#             raise ValueError("некорректное поле name")
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if type(name) != str or len(name) < 3 or len(name) > 50:
#             raise ValueError("некорректное поле name")
#         if set(name) < set(cls.CHARS_CORRECT):
#             raise ValueError("некорректное поле name")
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()


# class Factory:
#     @staticmethod
#     def build_sequence(self):
#         sp = []
#         return sp
#
#     @staticmethod
#     def build_number(string):
#         return int(string)
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
