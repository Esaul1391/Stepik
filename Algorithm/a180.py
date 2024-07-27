import random

class RandomizedSet(object):

    def __init__(self):
        self.val_list = []

    def check_val(self, val):
        return val in self.val_list

    def insert(self, val):
        if not self.check_val(val):
            self.val_list.append(val)
            return True  # Возвращаем True, если вставка успешна
        return False  # Возвращаем False, если элемент уже существует

    def remove(self, val):
        if self.check_val(val):
            self.val_list.remove(val)
            return True  # Возвращаем True, если удаление успешно
        return False  # Возвращаем False, если элемента нет в списке

    def getRandom(self):
        if not self.val_list:
            return None  # Возвращаем None, если список пуст
        return random.choice(self.val_list)

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()

param_1 = obj.insert(4)
param_2 = obj.remove(5)
param_3 = obj.getRandom()