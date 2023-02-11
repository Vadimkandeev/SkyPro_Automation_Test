from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By




driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.set_window_size(700, 800)

# Заходим на сайт--------------
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#---------------------------------

# 5 раз кликаем кнопку
find_button = driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']")
lst = [] # Создаем список в который занесем все записи о кнопках 

for i in range(5):
    find_button.click()
# Собираем список кнопок  `Delete`   
    lst.append(str(driver.find_element(By.CSS_SELECTOR, "button.added-manually"))) # Чтобы веб элеменнт занести в список, его нужно преобразовать в строку
#-----------------------------------

# Красиво распечатываем список в столбик
for x in range(len(lst)):
    print(lst[x])

#print(lst, sep="\n") # по какой то причине не работает 


sleep(2)

driver.close()