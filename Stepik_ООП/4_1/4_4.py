class User:
    def __init__(self, name, age):
        if type(name) == str and name.isalpha() and name.strip():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

        if isinstance(age, (int, float)) and 0 < int(age) < 110:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and name.isalpha() and name.strip():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, (int, float)) and 0 < int(age) < 110:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')

user = User('Меган', 37)

invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)