import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html', ]

with webdriver.Chrome() as driver:
    driver.get(sites[0])
    # i = driver.find_element(By.TAG_NAME, 'input')
    # i.click()
    # t = int(driver.find_element(By.ID, 'result').text)
    count = 0
    for site in sites[1:]:
        driver.execute_script('window.open("{}");'.format(site))

    all_pages = driver.window_handles

    for i in all_pages:
        driver.switch_to.window(i)
        k = driver.find_element(By.TAG_NAME, 'input')
        k.click()
        t = int(driver.find_element(By.ID, 'result').text)
        count += math.sqrt(t)

    print(round(count, 9))




# import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# response = requests.get('https://parsinger.ru/blank/3/index.html')
# print(response.status_code)
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/blank/3/index.html')
#     pages = driver.find_elements(By.TAG_NAME, 'input')
#     count = 0
#
#     for page in pages:
#         print(page)
#         page.click()
#         # time.sleep(0.1)
#
#     all_pages = driver.window_handles
#     for i in all_pages[1:]:
#         driver.switch_to.window(i)
#         # time.sleep(0.1)
#         try:
#             count += int(driver.execute_script("return document.title;"))
#         except ValueError:
#             print('No')
#
#     print(count)
