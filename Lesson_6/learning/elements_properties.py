from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
"""
driver.get("http://ya.ru")

driver.set_window_size(1000, 600)

txt = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").text
print(txt)

tag = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").tag_name
print(tag)

id = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").id
print(id)

href = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").get_attribute("href")
print(href)

ff = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").value_of_css_property("font-family")
print(ff)

color = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").value_of_css_property("color")
print(color)
"""
# driver.get("http://uitestingplayground.com/visibility")
# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)

# driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
# #elements.clear()
# #elements.send_keys("test skypro")
# sleep(2)

# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)

# driver.get("https://demoqa.com/radio-button")
# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
# print(is_enabled)


driver.get("https://the-internet.herokuapp.com/checkboxes")
# check_box = driver.find_element(By.CSS_SELECTOR,  "#checkboxes > input[type=checkbox]:nth-child(1)").is_selected()
# print(check_box)
# sleep(2)
# check_box = driver.find_element(By.CSS_SELECTOR,  "#checkboxes > input[type=checkbox]:nth-child(1)").click()
# check_box = driver.find_element(By.CSS_SELECTOR,  "#checkboxes > input[type=checkbox]:nth-child(1)").is_selected()
# print(check_box)


#div = driver.find_element(By.CSS_SELECTOR,  "#page-footer")

#a = div.find_element(By.CSS_SELECTOR, "a")

#print(a.get_attribute("href"))
divs = driver.find_elements(By.CSS_SELECTOR, "div")
div = divs[6]
css_class div.get_attribute("class")
print(css_class)
l = len(divs)
print(l)
sleep(5)
