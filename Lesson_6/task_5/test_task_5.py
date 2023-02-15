from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

sleep(48)
"""
waiter = WebDriverWait(driver, 48)

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[aria-valuenow]"), "75")
)
"""
res = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text 
def test_calc():  
    assert res == "15"



driver.quit()

