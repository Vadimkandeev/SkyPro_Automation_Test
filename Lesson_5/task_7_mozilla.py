from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.set_window_size(700, 800)

# Заходим на сайт--------------
driver.get("http://the-internet.herokuapp.com/inputs")
#---------------------------------


search_input = driver.find_element(By.CSS_SELECTOR, "[type='number']")
sleep(1) # Задержки введены для наглядности

search_input.send_keys("1000") #  Записываем в строку "1000"
sleep(1)

search_input.clear() # очищаем строку
sleep(1)

search_input.send_keys("SkyPro") # Записываем в строку  "SkyPro"
sleep(2)

driver.close() # Закрываем браузер