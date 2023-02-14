from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "[onclick='LoadLabel()']").click()

txt = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)