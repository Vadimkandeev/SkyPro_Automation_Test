from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Создаем словарь, в который заносим локатор и строку, которую надо вписать в поле
card = {
    0: ["[name='first-name']", "Иван", "#first-name"],       
    1: ["[name='last-name']", "Петров", "#last-name"],       
    2: ["[name='address']", "Ленина, 55-3", "#address"],   
    3: ["[name='zip-code']", "", "#zip-code"],             
    4: ["[name='city']", "Москва", "#city"],           
    5: ["[name='country']", "Россия", "#country"],         
    6: ["[name='job-position']", "QA", "#job-position"],        
    7: ["[name='company']", "SkyPro", "#company"],        
    8: ["[name='e-mail']", "SkyPro@hotmail.ru", "#e-mail"],
    9: ["[name='phone']", "89998887766", "#phone"]
}


# Заходим на сайт--------------
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
#---------------------------------


# Создаем функцию, которая будет отвечать  за запись строк в поля
def test_input_symbols_in_string(locator, txt):
# вписываем слово в строку
    driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("color")
    return color
    
# Создаем функцию, которая будет проверять цвет текстовых полей после нажатия кнопки "Применить"
def sheck_fields(locator):
    color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
    return color


# в цикле вызываем функцию и заносим значения в поля   
for i in range(len(card)):
    test_input_symbols_in_string(card[i][0], card[i][1])
    #print(test_input_symbols_in_string(card[i][0], card[i][1]))
    sleep(1)

# Жмякаем кнопку "применить"
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

"""
@pytest.mark.parametrize("locator", [
    card[0][2],
    card[1][2], 
    card[2][2], 
    card[3][2], 
    card[4][2],   # Не могу понять, почему эта функция не работает. Не могу отработать проверкку через Pytest
    card[4][2], 
    card[5][2], 
    card[6][2], 
    card[7][2], 
    card[8][2], 
    card[9][2],
    ])
def test_check(locator):
    #print(sheck_fields(locator)) 
    assert sheck_fields(locator) == "rgba(209, 231, 221, 1)"
"""
# В цикле вызываем функцию проверки цвета поля и воводим на печать 
for i in range(len(card)):
    if sheck_fields(card[i][2]) == "rgba(209, 231, 221, 1)":
        print(sheck_fields(card[i][2]), "is True")
    else:
         print(sheck_fields(card[i][2]), "is False")
sleep(3)

driver.quit()