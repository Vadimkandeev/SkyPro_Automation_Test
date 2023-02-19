from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://ya.ru")

driver.set_window_size(1000, 600)

elements = driver.find_element(By.CSS_SELECTOR, "#text")
elements.clear()
elements.send_keys("test skypro")


elements = driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()

#print(elements)

sleep(10)