import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from cookie import cookies


with webdriver.Chrome() as driver:
    url = 'https://parsinger.ru/selenium/5.6/1/index.html'
    response = requests.get(url)
    print(response.status_code)
    driver.get(url)
    for i in cookies:
        driver.add_cookie(i)
        driver.refresh()
    all_cookies = driver.get_cookies()
    time.sleep(60)

















# with webdriver.Chrome() as driver:
#     url = 'https://parsinger.ru/methods/5/index.html'
#     driver.get(url)
#     all_pages = driver.find_elements(By.CLASS_NAME, 'urls')
#     max_time = 0
#     need_page = ''
#     for page in all_pages:
#         link = page.find_element(By.TAG_NAME, 'a').get_attribute('href')
#         page.click()
#         t = driver.get_cookies()
#         expiry = int(t[0]['expiry'])
#         if max_time < expiry:
#             max_time = expiry
#             need_page = link
#         driver.back()
#     driver.get(need_page)
#     res = driver.find_element(By.ID, 'result').text
#     print(res)
#
# print(max_time, need_page)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# url = 'https://parsinger.ru/methods/3/index.html'
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     d = driver.get_cookies()
#     count = 0
#     for i in d:
#         check = int(i['name'].split('_')[-1])
#         if check % 2 == 0:
#             count += int(i['value'])
#
#
# print(count)

