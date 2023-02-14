from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



 
class Registrated:
   
    def browser(self):
        # Заходим на сайт--------------
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        #---------------------------------


    # Создаем функцию, которая будет отвечать  за запись строк в поля
    def input_first_name(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click() # кликаем по строке, чтоб активировать её
        first_name = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
        
        return first_name
        
    
    def input_last_name(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click()
        last_name = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
        
        return last_name


    def input_address(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click()
        address = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
        
        return address


    def input_zip_code(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click()
        zip_code = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
        
        return zip_code


    def input_city(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click()
        city = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
        
        return city


    def input_country(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click()
        country = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
        
        return country


    def input_job_position(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click()
        job_position = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
       
        return job_position


    def input_company(self,locator:str, txt:str):  
        driver.find_element(By.CSS_SELECTOR, locator).click()
        company = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
       
        return company


    def button_click(self,button):
        # Жмякаем кнопку "применить"
        driver.find_element(By.CSS_SELECTOR, button).click()



    # создаем функцию, которая будет проверять цвет каждого поля 
    def check_lield_first_name(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color


    def check_field_last_name(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color
    
    
    def check_field_address(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color


    def check_field_zip_code(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color
    

    def check_field_city(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color
    

    def check_field_country(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color


    def check_field_job_position(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color


    def check_field_company(self, locator):
        color = driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
        return color
    
    def quit_browser(self):
        driver.quit()