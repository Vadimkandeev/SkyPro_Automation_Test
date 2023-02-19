from selenium.webdriver.common.by import By    

                             
class MainPage:
    def __init__(self, driver, url:str): 
        self._driver = driver
        self._driver.get(url) 

    def input_username(self, username:str): # метод ввода имени юзера
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)

    def input_password(self, password:str): #  ввод пароля
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    def any_button_click(self, locator): #  Метод клика любой конпки
        self._driver.find_element(By.CSS_SELECTOR, locator).click()

    def fill_delivery_form(self): #  Метод заполнения формы для доставки
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Dart")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Vaider")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("111333444")  

    def order_confirmation(self): # получение конечной цены заказа
        txt = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text  
        return txt


