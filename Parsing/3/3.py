import requests
from collections import defaultdict
import json

url = 'https://parsinger.ru/3.4/3/dialog.json'

response = requests.get(url)
json_load = response.json()
common_dict = {}


def get_posts(lst):  # в функцию поступает список со словарями
    answer = {}  # это словарь-счетчик юзеров и постов
    for dct in lst:  # далее прохожу по каждому словарю в списке (lst - это dct['comments'])
        answer[dct['username']] = answer.get(dct['username'], 0) + 1  # добавляю юзера в мой словарь
        if not dct['comments']:  # если это крайний случай - ничего не делаю
            continue
        else:  # если не крайний, то ищу дальше, пока не нащупаю дно :)
            for key, value in get_posts(dct['comments']).items():
                answer[key] = answer.get(key, 0) + value
    return answer

print(list(json_load))
