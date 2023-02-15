from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    
lst = []


  
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
        
first_name = driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
lst.append(first_name)
last_name = driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
lst.append(last_name) 
address = driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
lst.append(address)
zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
lst.append(zip_code)
city = driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
lst.append(city)
country = driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
lst.append(country)
job_position = driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")
lst.append(job_position)
email = driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
lst.append(email)
phone = driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
lst.append(phone)
company = driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
lst.append(company)


@pytest.mark.xfail()  
def test_browser():
    assert lst[3] == "rgba(209, 231, 221, 1)"
    


driver.quit()