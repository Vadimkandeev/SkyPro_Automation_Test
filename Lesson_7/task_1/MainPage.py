from selenium.webdriver.common.by import By    

                             
class MainPage:
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
    
     
    
    # Создаем функцию, которая будет отвечать  за запись строк в поля
    def test_input_symbols_in_string(self,):
        card = {
        0: ["[name='first-name']", "Иван"],       
        1: ["[name='last-name']", "Петров"],       
        2: ["[name='address']", "Ленина, 55-3"],   
        3: ["[name='zip-code']", ""],             
        4: ["[name='city']", "Москва"],           
        5: ["[name='country']", "Россия"],         
        6: ["[name='job-position']", "QA"],        
        7: ["[name='company']", "SkyPro"],        
        8: ["[name='e-mail']", "SkyPro@hotmail.ru"],
        9: ["[name='phone']", "89998887766"]
        }
        for i in range(len(card)): 
            # вписываем слово в строку
            self._driver.find_element(By.CSS_SELECTOR, card[i][0]).send_keys(card[i][1])

               
    
    # Жмякаем кнопку "применить"
    def button_click(self, locator:str):
        self._driver.find_element(By.CSS_SELECTOR, locator).click()
        
   
    # регистрируем цвета полей после нажатия кнопки
    def check_first_name(self):
        first_name = self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
        return first_name
    def check_last_name(self):
        last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
        return last_name
    def check_address(self):
        address = self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
        return address
    def check_zip_code(self):
        zip_code = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code
    def check_city(self):
        city = self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
        return city
    def check_country(self):
        country = self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
        return country
    def check_job_position(self):
        job_position = self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")
        return job_position
    def check_company(self):
        company = self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
        return company
    def check_e_mail(self):
        e_mail = self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
        return e_mail
    def check_phone(self):
        phone = self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
        return phone

    """ 

    def check_fields(self):
        locators = {
        0: ["first_name", "#first-name"],       
        1: ["last_name", "#last-name"],         # Пока не придумал, как применить этот метод 
        2: ["address","#address"],   
        3: ["zip_code", "#zip-code"],             
        4: ["city", "#city"],           
        5: ["country", "#country"],         
        6: ["job_position", "job_position"],        
        7: ["company", "#company"],        
        8: ["e_mail", "#e_mail"],
        9: ["phone", "#phone"]
        }
        for i in range(len(locators)): 
            locators[i][0] = self._driver.find_element(By.CSS_SELECTOR, locators[i][1]).value_of_css_property("background-color")
            return locators[i][0]   
  """   