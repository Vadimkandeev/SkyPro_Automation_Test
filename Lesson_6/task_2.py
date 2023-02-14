from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Заходим на сайт--------------
driver.get("http://uitestingplayground.com/textinput")
#---------------------------------

# кликаем по строке, чтоб активировать её
driver.find_element(By.CSS_SELECTOR, ".form-control").click()

# вписываем слово в строку
find_string = driver.find_element(By.CSS_SELECTOR, ".form-control")
find_string.send_keys("SkyPro")

# жмякаем кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# считываем надпись с кнопки
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# вывод на печать надписи
print(txt)
