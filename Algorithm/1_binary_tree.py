# example

def binary_search(lst, item):
    low = 0                 # Нижний индекс массива
    high = len(lst) - 1     # Верхний индекс массива

    while low <= high:      # Пока нижний индекс не превышает верхний
        mid = (low + high) // 2   # Находим средний индекс (целочисленное деление)
        guess = lst[mid]          # Получаем значение в середине массива

        if guess == item:         # Если угадали
            return mid            # Возвращаем индекс элемента
        if guess > item:          # Если угаданное значение больше искомого
            high = mid - 1        # Сужаем диапазон до левой половины
        else:
            low = mid + 1         # Иначе сужаем диапазон до правой половины

    return None                   # Если элемент не найден, возвращаем None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1 (индекс числа 3 в массиве)
print(binary_search(my_list, -1)) # => None (число -1 не найдено в массиве)
