from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage




browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    
def test_color_fields(): 
    
    main_page = MainPage(browser)  
    
    main_page.test_input_symbols_in_string()  #  вызываем метод ввода текста в поля

    main_page.button_click("[type='submit']")   # клик на кнопку "Принять"

    # вызываем методы  проверки цвета текстовых полей
    first_name = main_page.check_first_name()
    last_name = main_page.check_last_name()
    address = main_page.check_address()
    zip_code = main_page.check_zip_code()
    city = main_page.check_city()
    country = main_page.check_country()
    job_position = main_page.check_job_position()
    company = main_page.check_company()
    e_mail = main_page.check_e_mail()
    phone = main_page.check_phone()

    assert  first_name == "rgba(209, 231, 221, 1)"
    assert  last_name == "rgba(209, 231, 221, 1)"
    assert  address == "rgba(209, 231, 221, 1)"
    assert  zip_code == "rgba(248, 215, 218, 1)"
    assert  city == "rgba(209, 231, 221, 1)"
    assert  country == "rgba(209, 231, 221, 1)"
    assert  job_position == "rgba(209, 231, 221, 1)"
    assert  company == "rgba(209, 231, 221, 1)"
    assert  e_mail == "rgba(209, 231, 221, 1)"
    assert  phone == "rgba(209, 231, 221, 1)"
    
    browser.quit()


