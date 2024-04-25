import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as driver:
    driver.get(url='https://parsinger.ru/selenium/5.10/3/index.html')
    containers = driver.find_elements(By.CSS_SELECTOR, '[class^="draganddrop"]')

    actions = ActionChains(driver)
    for i in range(0, len(containers), 2):
        actions.drag_and_drop(containers[i], containers[i+1]).perform()
        # time.sleep()

    # time.sleep(10)
    res = driver.find_element(By.ID, 'message')
    print(res.text)



# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.10/2/index.html')
#     squars = driver.find_elements(By.CSS_SELECTOR, '[class^="draganddrop"]')
#     target = driver.find_element(By.CLASS_NAME, 'draganddrop_end')
#
#
#     for element in squars:
#         actions = ActionChains(driver)
#         actions.drag_and_drop(element, target).perform()
#         time.sleep(0.1)
#     res = driver.find_element(By.ID, 'message').text
#
#     print(res)