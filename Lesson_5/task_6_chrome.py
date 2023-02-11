from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(700, 800)

# Заходим на сайт--------------
driver.get("http://the-internet.herokuapp.com/entry_ad")
#---------------------------------

sleep(2)
#  кликаем кнопку в модальном окне
find_button_click_here = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > p")
find_button_click_here.click()

    

sleep(2)