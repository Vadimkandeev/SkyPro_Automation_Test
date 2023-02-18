from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_internet_store():  # начальная страница. Заполняем поля, осуществляем вход
    test_int_store = MainPage(browser, "https://www.saucedemo.com/" )
    test_int_store.input_username("standard_user")
    test_int_store.input_password("secret_sauce")
    test_int_store.any_button_click("#login-button")

    # переход на страницу каталога, добавление товаров в корзину
    test_int_store = MainPage(browser, 'https://www.saucedemo.com/inventory.html' )
    test_int_store.any_button_click("#add-to-cart-sauce-labs-backpack")
    test_int_store.any_button_click("#add-to-cart-sauce-labs-bolt-t-shirt")
    test_int_store.any_button_click("#add-to-cart-sauce-labs-onesie")
    
    # переход к корзине
    test_int_store = MainPage(browser, 'https://www.saucedemo.com/cart.html' )
    test_int_store.any_button_click("#shopping_cart_container")
    test_int_store.any_button_click("#checkout")

    # переход к зполнению формы для доставик заказа
    test_int_store = MainPage(browser, 'https://www.saucedemo.com/checkout-step-one.html') 
    test_int_store.fill_delivery_form()
    test_int_store.any_button_click("#continue")
    
    # получение конечной суммы заказа для сверки
    test_int_store = MainPage(browser, "https://www.saucedemo.com/checkout-step-two.html")
    summ = test_int_store.order_confirmation()

    browser.quit()
   
    assert summ == "Total: $58.29"





