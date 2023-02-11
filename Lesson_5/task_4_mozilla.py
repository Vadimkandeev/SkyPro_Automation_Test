from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.set_window_size(700, 800)

# Заходим на сайт--------------
driver.get("http://uitestingplayground.com/dynamicid")
#---------------------------------

# 3 раза кликаем кнопку
find_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
for i in range(3):
    find_button.click()
    print(find_button.click) # убеждаемся что кнопка работает
print("Кнопка работает. Но это не точно")   

sleep(2)

driver.close()