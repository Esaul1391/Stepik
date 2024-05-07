import requests
from bs4 import BeautifulSoup
import json


response = requests.get(url="https://parsinger.ru/4.8/6/index.html")
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")


specifications = soup.find_all('tr')
common_data = []
for row in specifications[1:]:
    row = [i.text for i in row]
    if int(row[-1]) <= 4000000 and int(row[1]) >= 2005 and row[4] == 'Бензиновый':
        d = {
            "Марка Авто": row[0],
            "Год выпуска": int(row[1]),
            "Тип двигателя": row[4],
            "Стоимость авто": int(row[-1])
        }
        common_data.append(d)
res = sorted(common_data, key=lambda x: x["Стоимость авто"], reverse=False)
print(json.dumps(res, indent=4, ensure_ascii=False))
