from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from Calculator import Calculator


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_check_calculator_result():
    calculator = Calculator(browser) 
    calculator.clear_field_delay("15")
    calculator.key_pressed()
    calculator.delay_after("15")
    result =  calculator.result()

    assert result == "15"
    browser.quit()
