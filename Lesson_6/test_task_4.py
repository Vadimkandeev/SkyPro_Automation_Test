from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    

  
driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")

driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")

driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")

driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys("")

driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")

driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")

driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")

driver.find_element(By.CSS_SELECTOR, "[name='e-mail']",).send_keys("SkyPro@hotmail.com")

driver.find_element(By.CSS_SELECTOR, "[name='phone']",).send_keys("89995556644")

driver.find_element(By.CSS_SELECTOR, "[name='company']",).send_keys("SkyPro")

    
    # Жмякаем кнопку "применить"
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

# регистрируем цвета полей после нажатия кнопки     
first_name = driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")

address = driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")

zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")

city = driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")

country = driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")

job_position = driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")

email = driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")

phone = driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")

company = driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")



# Проверяем цвета полей с корректным вводом данных
@pytest.mark.parametrize("field", [
    first_name, 
    last_name, 
    address, 
    city, 
    country, 
    job_position, 
    email, 
    phone, 
    company
    ])
def test_fields(field):
    assert field == "rgba(209, 231, 221, 1)"

# Проверяем цвет поля с ошибкой ввода данных
@pytest.mark.xfail()  
def test_browser():
    assert zip_code == "rgba(209, 231, 221, 1)"
    


driver.quit()