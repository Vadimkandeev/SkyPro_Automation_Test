from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
