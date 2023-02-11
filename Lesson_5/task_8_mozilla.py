from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.set_window_size(700, 800)

# Заходим на сайт--------------
driver.get("http://the-internet.herokuapp.com/login")
#---------------------------------

#  Записываем в строку "tomsmith"
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith") 
sleep(1)

#  Записываем в строку "SuperSecretPassword!"
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!") 
sleep(1)
#  клик по кнопке "Login"
login_button =  driver.find_element(By.CSS_SELECTOR, ".fa")
login_button.click()

sleep(2)

driver.close()