from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
cookie = {
    "name": "cookie_policy",
    "value": "1"
}

def test_cart_counter():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.labirint.ru/")
    driver.add_cookie(cookie)
# Зайти в Лабиринт
# cookies = driver.get_cookies()
# print(cookies)
# driver.refresh()
# driver.delete_all_cookies()
# driver.refresh()
# sleep(10)
#driver.quit()
