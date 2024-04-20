import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

with webdriver.Chrome() as driver:
    url = 'https://parsinger.ru/selenium/5.5/5/1.html'
    driver.get(url)
    containers = driver.find_element(By.ID, 'main-container').find_elements(By.TAG_NAME, 'div')
    count = 0
    for elem in containers:

        try:
            color_code = elem.find_element(By.TAG_NAME, 'span').text
            cascade = elem.find_element(By.TAG_NAME, 'select')
            select = Select(cascade)
            cascade.send_keys(color_code)       # Выбирает из каскада элементов
            time.sleep(0.2)
            choose_color = elem.find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'button')
            for button in choose_color:
                if button.get_attribute('data-hex') == color_code:
                    button.click()
                    time.sleep(0.1)
                    break
            check_box = elem.find_elements(By.TAG_NAME, 'input')
            check_box[0].click()
            check_box[1].send_keys(color_code)
            check = elem.find_elements(By.TAG_NAME, 'button')[-1].click()
            count += 1
        except Exception:
            print('-')

    last_check = driver.find_element(By.XPATH, '/html/body/button').click()
    print(driver.switch_to.alert.text)
# //*[@id="main-container"]/div[2]/div
# get_attribute('data-hex')

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
#
# with webdriver.Chrome() as driver:
#     url = 'https://parsinger.ru/selenium/5.5/4/1.html'
#     driver.get(url)
#     field = driver.find_elements(By.CLASS_NAME, 'parent')
#     for element in field:
#         num_sp = element.find_elements(By.TAG_NAME, 'textarea')
#         button = element.find_element(By.TAG_NAME, 'button')
#         num_sp[-1].send_keys(num_sp[0].text)
#         num_sp[0].clear()
#         button.click()
#         time.sleep(0.1)
#     driver.find_element(By.ID, 'checkAll').click()
#     time.sleep(4)
#     res = driver.find_element(By.ID, 'congrats').text
#     print(res)





# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as driver:
#     url = 'https://parsinger.ru/selenium/5.5/3/1.html'
#     driver.get(url)
#     find_box = driver.find_elements(By.CLASS_NAME, 'parent')
#     count = 0
#     for i in find_box:
#         check_box = i.find_element(By.CLASS_NAME, 'checkbox')
#         if check_box.is_selected():
#             num = i.find_element(By.TAG_NAME, 'textarea').text
#             count += int(num)
# print(count)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as driver:
#     url = 'https://parsinger.ru/selenium/5.5/2/1.html'
#     driver.get(url)
#     clear_box = driver.find_elements(By.CLASS_NAME, 'text-field')
#     for i in clear_box:
#         if i.get_attribute('data-enabled'):
#             i.clear()
#
#     button = driver.find_element(By.TAG_NAME, 'button')
#     button.click()
#     print(driver.switch_to.alert.text)








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