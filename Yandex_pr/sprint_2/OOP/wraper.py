# global_variable = 'Глобальная'
#
#
# def some_func(passed_variable):
#     local_variable = 'Локальная'
#
#     def inside_func():
#         inside_local_variable = 'Внутренняя'
#         return (f'{global_variable} '
#                 f'{local_variable} '
#                 f'{passed_variable} '
#                 f'{inside_local_variable}')
#     return inside_func
#
# # Здесь вызывается функция some_func()
# # и результат её работы присваивается переменной kind_of_magic
# kind_of_magic = some_func('Параметр')
#
# # Здесь рождается магия: some_func() вернула функцию,
# # значит, kind_of_magic — это функция
# # и её можно вызвать:
# print(kind_of_magic())
# Будет напечатано: Глобальная Локальная Параметр Внутренняя

# # Можно создать ещё одну функцию
# another_magic = some_func('Другой параметр')
# print(another_magic())
# # Будет напечатано: Глобальная Локальная Другой параметр Внутренняя

# global_variable = 'Глобальная'
#
#
# def some_func(passed_variable):
#     local_variable = 'Локальная'
#
#     def inside_func():
#         inside_local_variable = 'Внутренняя'
#         return(f'{global_variable} '
#                f'{local_variable} '
#                f'{passed_variable} '
#                f'{inside_local_variable}')
#     return inside_func
#
# # Создали две функции
# kind_of_magic = some_func('Параметр')
# another_magic = some_func('Другой параметр')
#
# del some_func  # Уничтожили функцию some_func()
#
# # Всё равно сработает
# print(kind_of_magic())
# # Будет напечатано: Глобальная Локальная Параметр Внутренняя
#
# print(another_magic())
# # Будет напечатано: Глобальная Локальная Другой параметр Внутренняя
#
# # А это уже не сработает:
# # some_func() удалена, создать новую функцию не получится.
# misery_of_magic = some_func('Пробуем последний раз')
# # NameError: name 'some_func' is not defined

# def some_func(passed_variable):
#     def inside_func(passed_inside_variable):
#         return f'{passed_variable}, {passed_inside_variable}'
#     return inside_func
#
# # Создали функцию hello()
# hello = some_func('Привет')
# # В контексте функции hello() значением passed_variable будет строка 'Привет'
#
# # Вызваем hello() с параметром для inside_func()
# print(hello('Стёпа'))
# # Будет напечатано: Привет, Стёпа
#
# byebye = some_func('До свидания')
# # В контексте функции byebye()
# # значением passed_variable будет строка 'До свидания'
#
# print(byebye('Марк Лутц'))
# # Будет напечатано: До свидания, Марк Лутц
#
# # Но значение переменной passed_variable в контексте hello() cохранилось:
# # оно по-прежнему 'Привет'
# print(hello('Лера'))
# Будет напечатано: Привет, Лера


# В зависимости от уровня сложности (volume)
# функция возвращает различное написание фразы.
# def speech(text, volume):
#     def whisper():
#         return f'{text.lower()}...'
#
#     def scream():
#         return f'{text.upper()}!!!11'
#
#     if volume < 50:
#         return whisper
#     return scream
#
# easy_closure = speech('Замыкание - это просто', 40)
# print(easy_closure())
# # Будет напечатано: ЗАМЫКАНИЕ - ЭТО ПРОСТО!!!11

def make_divider_of(divider):
    def division_operation(divisible):
        return divisible / divider

    return division_operation


# Создали функцию

div2 = make_divider_of(2)
print(div2(10))  # Такой вызов должен вернуть 10/2, то есть 5.0

div5 = make_divider_of(5)

print(div5(20))  # Такой вызов должен вернуть 4.0

print(div5(div2(20)))  # Такой вызов должен вернуть 2.0
