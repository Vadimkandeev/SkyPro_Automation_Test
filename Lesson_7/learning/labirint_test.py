from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    "name": "cookie_policy",
    "value": "1"
}
def test_cart_counter(): 
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Зайти в Лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

    # найти все книги по слову Питон
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("Python")
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    sleep(5)
    # переключиться на таблицу  ".btn.buy-link.btn-primary"
    browser.find_element(By.CSS_SELECTOR, "a[title='таблицей']").click()

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))
    sleep(6)
    # добавить все книги в корзину и посчитать их количество
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    browser.get("https://www.labirint.ru/cart/")  
    
    # проверить счетчик товаров. Должен быть равен числу кликов
    a = browser.find_element(By.CSS_SELECTOR, "[data-event-label='myCart']")
     #получить текущее значение
    txt = a.find_element(By.CSS_SELECTOR, "b").text

    #сравнить его с counter
    assert counter == int(txt)  
       
    


    browser.quit()




