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

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def open_labirint():    # Зайти в Лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def search(term):
    # найти все книги по слову Питон
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def switch_to_table():
     # переключиться на таблицу  ".btn.buy-link.btn-primary"
    browser.find_element(By.CSS_SELECTOR, "a[title='таблицей']").click()

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))

def add_books():
     # добавить все книги в корзину и посчитать их количество
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1 
    return counter       


def go_to_cart(): # перейти в корзину
    browser.get("https://www.labirint.ru/cart/") 

def get_cart_counter():
    # проверить счетчик товаров. Должен быть равен числу кликов
    a = browser.find_element(By.CSS_SELECTOR, "[data-event-label='myCart']")
     #получить текущее значение
    txt = a.find_element(By.CSS_SELECTOR, "b").text
    return int(txt)

def close_driver():
    browser.quit()

def test_cart_counter(): 

    open_labirint()
    search("Python")
    switch_to_table()
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()

    assert added == cart_counter

    




