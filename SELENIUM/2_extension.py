import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')
# options_chrome.add_extension('coordinates.crx')


with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(5)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.chrome.service import Service as ChromiumService
#
# url = 'https://2ip.ru/'
# with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
#
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)