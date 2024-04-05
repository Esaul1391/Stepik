import requests
import json
from collections import defaultdict


headers = {
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
    'Referer': 'https://parsinger.ru/4.6/1/index.html',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://parsinger.ru/4.6/1/res.json', headers=headers).json()
d = defaultdict(int)
for cart in response:
    d[cart["categories"]] += int(cart["article"]) * int(cart["description"]["rating"])

print(d)

# url = 'https://parsinger.ru/downloads/get_json/res.json'
# sp = []
# d = defaultdict(int)
# response = requests.get(url).json()
# for item in response:
#     d[item["categories"]] += (int(item["count"]) * int(item["price"].split(' ')[0]))
#     print(item["categories"], int(item["count"]))
#
# print(d)





# import requests
# from bs4 import BeautifulSoup
# import json
#
# result_json = []
#
# for i in range(1, 33):
#     url = f'https://parsinger.ru/html/mobile/2/2_{i}.html'
#     response = requests.get(url)
#     response.encoding = 'utf-8'
#
#     soup = BeautifulSoup(response.text, 'lxml')
#     name = soup.find('p', id='p_header').text.strip()
#     article = soup.find('p', class_='article').text.split(':')[-1].strip()
#     value_description = [i.text.split(':')[1].strip() for i in soup.find_all('li')]
#     name_descriptions = ["brand", "model", "type", "material", "type_display", "diagonal", "size", "weight", "resolution", "site"]
#     description = dict(zip(name_descriptions, value_description))
#     count = soup.find('span', id='in_stock').text.split(': ')[-1].strip()
#     price = soup.find('span', id='price').text.strip()
#     old_price = soup.find('span', id='old_price').text.strip()
#     sp = {
#         "categories": "mobile",
#         "name": name,
#         "article": article,
#         "description": description,
#         "count": count,
#         "price": price,
#         "old_price": old_price,
#         "link": url
#     }
#     result_json.append(sp)

# import requests
# from bs4 import BeautifulSoup
# import json
#
# result_json = []
# for k in range(1, 6):
#     for num_page in range(1, 5):
#         url = f'https://parsinger.ru/html/index{k}_page_{num_page}.html'
#         response = requests.get(url)
#         response.encoding = 'utf-8'
#
#         soup = BeautifulSoup(response.text, 'lxml')
#         carts = soup.find_all('div', class_='item')
#
#         for cart in carts:
#             sp = []
#             name = cart.find('a', class_='name_item').text.strip()
#             description = cart.find('div', class_='description').find_all('li')
#             description = [i.text.strip().split(': ') for i in description]
#             description = [(i[0], i[1].strip()) for i in description]
#             price = cart.find('p', class_='price').text.strip()
#             sp.append(("Наименование", name))
#             sp.extend(description)
#             sp.append(("Цена", price))
# #             d = dict(sp)
# #             result_json.append(d)
# with open('json_file.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# #
# # print(result_json)