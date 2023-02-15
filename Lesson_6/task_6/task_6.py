from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")  

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")