import requests
import csv
import lxml
from bs4 import BeautifulSoup

with open('my_csv.csv', 'w', encoding='utf-8', newline='') as file:
    col_name = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
                'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
                'Ссылка на карточку с товаром']
    writer = csv.writer(file, delimiter=';')
    writer.writerow(col_name)

for i in range(1, 5):
    url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    carts = soup.find_all('div', class_='item')
    for cart in carts:
        sp_cart = []
        name = cart.find('a', class_='name_item')
        print(name)




