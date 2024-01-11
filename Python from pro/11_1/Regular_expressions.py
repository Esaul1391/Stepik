def get_biggest(numbers):
    if not numbers:
        return -1

    # Преобразуем числа в строки, чтобы можно было сравнивать лексикографически
    numbers_str = []
    for i in numbers:
        if len(str(i)) == 1:
            numbers_str.append(str(i))
        else:
            while len(str(i)) != 1:
                i = i%10
                numbers_str.append(i)

    # # Сортируем строки в обратном порядке (чтобы получить наибольшее число)
    # numbers_str.sort(reverse=True)
    #
    # # Объединяем строки в одну
    # result_str = ''.join(numbers_str)

    return numbers_str

print(get_biggest([7, 71, 72]))

# import re
# import sys
#
# def parse_phone_number(phone_number):
#     # Паттерн для извлечения кода страны, кода города и номера
#     pattern = re.compile(r'(?P<country>\d{1,3})[-\s](?P<city>\d{1,3})[-\s](?P<number>\d{4,10})')
#
#     # Поиск соответствия паттерну в строке
#     match = pattern.search(phone_number)
#
#     if match:
#         # Извлечение данных из объекта match
#         country_code = match.group('country')
#         city_code = match.group('city')
#         phone_number = match.group('number')
#
#         # Вывод результата
#         print(f'Код страны: {country_code}, Код города: {city_code}, Номер: {phone_number}')
#     else:
#         print('Неверный формат номера')
#
# # Ввод и обработка номеров
# # while True:
# #     phone_number = input()
# #     if not phone_number:
# #         break
# #     parse_phone_number(phone_number)
#
#
#
#
# # data = [line.strip() for line in sys.stdin]
# for num in sys.stdin.read().splitlines():
#     parse_phone_number(num)



# from re import fullmatch
#
# match1 = fullmatch(r'(-)?(\d+)', '-2077')
# match2 = fullmatch(r'(-)?(\d+)', '-1337')
#
# print(match1.group(1))
# print(match1.group(2))
# print(match2.group(1, 2))




# from re import match
#
# match1 = match(r'[Hh]\w+', 'hello, Timur')
# match2 = match(r'[Tt]\w+', 'hello, Timur')
#
# print(match1.group() if match1 else None)
# print(match2.group() if match2 else None)

# pattern_7 = r'7-\d{3}-\d{3}-\d{2}-\{d2}'
# pattern_8 = r'8-\d{3}-\d{4}-\d{4}'
# import re
# def find_num(text):
#     print(re.findall(pattern_8 | pattern_7, text))
#     print(re.findall(pattern_7, text))
# find_num('Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911')
# import re
# pattern_7 = r'7-\d{3}-\d{3}-\d{2}-\{d2}'
# pattern_8 = r'8-\d{3}-\d{4}-\d{4}'
#
# def find_num(text):
#     #print(re.findall(pattern_8, text))
#     print(re.findall(r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}', text))
# find_num('Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911')
# find_num('Перезвони мне, пожалуйста: 8-919-6674-2119')
#
# regex = r'\d[aeiouy][^bcDF]\S[AEIOUY][^.,]'
