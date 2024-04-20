from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.9/6/index.html')




# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# res_text = ''
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.9/5/index.html')
#     squarer = driver.find_elements(By.CLASS_NAME, 'box_button')
#     for b in squarer:
#         b.click()
#         banner = driver.find_element(By.ID, 'close_ad')
#         banner.click()
#         element = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(banner))
#         time.sleep(6)
#         res_text += f''
#         print(b.text)






# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.9/4/index.html')
#     close = driver.find_element(By.CLASS_NAME, 'close')
#     close.click()
#     element = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(close))
#     button = driver.find_element(By.TAG_NAME, 'button')
#     button.click()
#     res = driver.find_element(By.ID, 'message').text
#     print(res)
#     time.sleep(4)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
#                'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.9/3/index.html')
#     locators = [(By.ID, id_) for id_ in ids_to_find]
#     for locator in locators:
#         click = False
#         while not click:
#             try:
#                 element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
#                 element.click()
#                 click = True
#             except:
#                 print('Давай еще')
#             print(1)
#     alert = driver.switch_to.alert.text
#     print(alert)
