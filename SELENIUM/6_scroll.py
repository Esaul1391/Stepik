from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_2/')

    action = ActionChains(driver)
    p_tags = driver.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "p")
    for i in p_tags:
        print(i)








# import pdb
# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     for i in range(2):
#         action = ActionChains(browser)
#         ActionChains(browser).move_to_element(browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')).scroll_by_amount(0, 1000).perform()
#         time.sleep(0.1)
#     p_tags = browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "p")
#     count = sum(int(tag.text) for tag in p_tags)








        # time.sleep(1)
        # scroll_origin = p_tags[-1]
        # scroll_origin = ScrollOrigin.from_element(scroll_origin)

        # action.scroll_from_origin(scroll_origin, 0, 200).perform()
        # action.move_to_element(scroll_origin).perform()


# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')
#     time.sleep(3)
#     tags_input = browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')
#     for i in range(300):
#         try:
#             tags_input[-1].send_keys(Keys.DOWN)
#         except Exception:
#             print('-')
#
#     tags_p = browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')
#     common_sum =[int(i.text) for i in tags_p]
#     print(sum(common_sum))


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/infiniti_scroll_1/')
#     container = driver.find_element(By.CLASS_NAME, 'scroll-container')
#     actions = ActionChains(driver)
#     actions.move_to_element(container).perform()
#     time.sleep(4)
#     while True:
#         ActionChains(driver).move_to_element(container).scroll_by_amount(1, 500).perform()
#         time.sleep(1)





# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# with webdriver.Chrome() as driver:
#     url = 'https://parsinger.ru/selenium/5.7/5/index.html'
#     driver.get(url)
#     buttons = driver.find_elements(By.TAG_NAME, 'button')
#     max_time = max([float(i.get_attribute('value')) for i in buttons])
#     print(max_time)
#     actions = ActionChains(driver)
#     for i in buttons:
#         actions.click_and_hold(i).perform()
#         actions.pause(max_time).perform()
#         actions.release(i).perform()
#     time.sleep(4)
#     print(driver.switch_to.alert.text)