from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class Calculator:


    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    
    def clear_field_delay(self, time:str):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)
        
    
    def key_pressed(self):
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)').click()
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)').click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()


    def delay_after(self, time:str): 
        WebDriverWait(self._driver, 48).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), time))


    def result(self):
        res = self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.top > div').text 
        return res