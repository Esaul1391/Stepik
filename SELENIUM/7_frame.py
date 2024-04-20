import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
with webdriver.Chrome(options=chrome_options) as driver:
    url = 'https://parsinger.ru/window_size/2/index.html'
    driver.get(url)


    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    d = {}
    for x, y in product(window_size_x, window_size_y):
        driver.set_window_size(x , y )
        res = driver.find_element(By.ID, 'result').text
        if res:
            print(res)
            d['width'] = x
            d['height'] = y
            print(d)








# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as driver:
#     url = 'https://parsinger.ru/selenium/5.8/5/index.html'
#     driver.get(url)
#
#     all_frame = driver.find_elements(By.TAG_NAME, 'iframe')
#     print(len(all_frame))
#     for frame in all_frame:
#         driver.switch_to.frame(frame)
#         time.sleep(1)
#         button = driver.find_element(By.CSS_SELECTOR, 'body > button').click()
#         # button.click()
#         num = driver.find_element(By.TAG_NAME, 'p').text
#         time.sleep(1)
#         print(num)
#         driver.switch_to.default_content()
#         input_value = driver.find_element(By.TAG_NAME, 'input')
#         input_value.clear()
#         input_value.send_keys(num)
#         driver.find_element(By.ID, 'checkBtn').click()
#         try:
#             res = driver.switch_to.alert.text
#             print(res)
#         except:
#             pass
