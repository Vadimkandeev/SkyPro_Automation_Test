from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.set_window_size(700, 800)

# Заходим на сайт--------------
driver.get("http://uitestingplayground.com/classattr")
#---------------------------------

# 3 раза кликаем кнопку
find_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.btn-test")
for i in range(3):
    find_button.click()
    sleep(1)  
    Alert(driver).accept() # сворачиваем модальное окно
    

sleep(2)

driver.close()