from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Страница авторизации 
driver.get('https://www.saucedemo.com/')

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")     
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

# переход на страницу каталога товаров
driver.get('https://www.saucedemo.com/inventory.html')

#Alert(driver).accept() # сворачиваем модальное окно

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

# переход в корзину
driver.get('https://www.saucedemo.com/cart.html')
driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()   

# Страница заполнения данных для заказа
driver.get('https://www.saucedemo.com/checkout-step-one.html')
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Dart")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Vaider")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("111333444")
driver.find_element(By.CSS_SELECTOR, "#continue").click()

# переход на страницу подтверждения заказа
driver.get("https://www.saucedemo.com/checkout-step-two.html")
txt = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]').text

driver.quit()
print(txt)
assert txt == "Total: $58.29"