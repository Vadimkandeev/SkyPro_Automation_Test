from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

driver.implicitly_wait(47)

def test_calc():
    res = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text
    print(res)
    assert res == "15"



driver.quit()

