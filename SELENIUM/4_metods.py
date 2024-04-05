import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    url = 'https://parsinger.ru/selenium/5.5/2/1.html'
    driver.get(url)
    clear_box = driver.find_elements(By.CLASS_NAME, 'text-field')
    for i in clear_box:
        if i.get_attribute('data-enabled'):
            i.clear()

    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    print(driver.switch_to.alert.text)








# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
#
# with webdriver.Chrome() as driver:
#     url = 'https://parsinger.ru/selenium/5.5/1/1.html'
#     driver.get(url)
#     text_fields = driver.find_elements(By.CLASS_NAME, 'text-field')
#     for i in text_fields:
#         i.clear()
#
#     button_check = driver.find_element(By.TAG_NAME, 'button')
#     button_check.click()
#     time.sleep(2)
#     print(driver.switch_to.alert.text)



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/methods/1/index.html'
# with webdriver.Chrome() as driver:
#     driver.get(url)
#
#     count = 0
#     while True:
#         driver.refresh()
#         count += 1
#         res = driver.find_element(By.ID, 'result').text
#         if res != 'refresh page':
#             print(count)
#             print(res)
#             break
#     print(res)