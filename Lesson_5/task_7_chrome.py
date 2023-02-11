from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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