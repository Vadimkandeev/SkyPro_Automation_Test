from task_4 import Registrated

import pytest


def browser_():
    registrated = Registrated()
    registrated.browser()
        
# заполняем поля  
@pytest.mark.parametrize("locator, data", ["[name='first-name']", "Иван"])
def fill_field_first_name(locator, data):
    registrated = Registrated()
    registrated.input_first_name(locator, data)



@pytest.mark.parametrize("locator, data", ["[name='last-name']", "Петров"])
def fill_field_last_name(locator, data):
    registrated = Registrated()
    registrated.input_last_name(locator, data)
    
    
@pytest.mark.parametrize("locator, data", ["[name='address']", "Ленина, 55-3"])
def fill_field_last_name(locator, data):
    registrated = Registrated()
    registrated.input_address(locator, data)


@pytest.mark.parametrize("locator, data", ["[name='zip-code']", "", "#zip-code"])
def fill_field_last_name(locator, data):
    registrated = Registrated()
    registrated.input_zip_code(locator, data)


@pytest.mark.parametrize("locator, data", ["[name='city']", "Москва"])
def fill_field_last_name(locator, data):
    registrated = Registrated()
    registrated.input_city(locator, data)


@pytest.mark.parametrize("locator, data", ["[name='country']", "Россия"])
def fill_field_last_name(locator, data):
    registrated = Registrated()
    registrated.input_country(locator, data)


@pytest.mark.parametrize("locator, data", ["[name='job-position']", "QA"])
def fill_field_last_name(locator, data):
    registrated = Registrated()
    registrated.input_job_position(locator, data)


@pytest.mark.parametrize("locator, data", ["[name='company']", "SkyPro"])
def fill_field_last_name(locator, data):
    registrated = Registrated()
    registrated.input_company(locator, data)
#----------------------------------------------------------------------


# жмем на кнопку "Применить"
def click():
    registrated = Registrated()
    registrated.button_click()


#  Проводим проверку  цвета полей ввода
@pytest.mark.parametrize("#first-name")    
def color_field_first_name(locator):
    registrated = Registrated()
    f_color = registrated.check_lield_first_name(locator)
    assert f_color == "rgba(209, 231, 221, 1)"



@pytest.mark.parametrize("#last-name")    
def color_field_last_name(locator):
    registrated = Registrated()
    f_color = registrated.check_field_last_name(locator)
    assert f_color == "rgba(209, 231, 221, 1)"


@pytest.mark.parametrize("#address")    
def color_field_address(locator):
    registrated = Registrated()
    f_color = registrated.check_field_address(locator)
    assert f_color == "rgba(209, 231, 221, 1)"


@pytest.mark.xfail("#zip-code")    
def color_field_zip_code(locator):
    registrated = Registrated()
    f_color = registrated.check_field_zip_code(locator)
    assert f_color == "rgba(209, 231, 221, 1)"



@pytest.mark.parametrize("#city")    
def color_field_city(locator):
    registrated = Registrated()
    f_color = registrated.check_field_city(locator)
    assert f_color == "rgba(209, 231, 221, 1)"


@pytest.mark.parametrize("#country")    
def color_field_country(locator):
    registrated = Registrated()
    f_color = registrated.check_field_country(locator)
    assert f_color == "rgba(209, 231, 221, 1)"


@pytest.mark.parametrize("#job-position")    
def color_field_job_position(locator):
    registrated = Registrated()
    f_color = registrated.check_field_job_position(locator)
    assert f_color == "rgba(209, 231, 221, 1)"


@pytest.mark.parametrize("#company")    
def color_field_company(locator):
    registrated = Registrated()
    f_color = registrated.check_field_company(locator)
    assert f_color == "rgba(209, 231, 221, 1)"
#---------------------------
    
# Закрываем браузер    
def browser_close():
    registrated = Registrated()
    registrated.quit_browser()
   