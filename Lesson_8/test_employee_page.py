from EmployeeClass import EmployeeClass
import pytest


driver = EmployeeClass('https://x-clients-be.onrender.com/employee')
                        
# Запрос всего списка сотрудников 
# 
# Позитивная проверка

def test_positive_get_workers_list():
    #  get list from API
    path = '?company='
    id = 251
    resp_api_json = driver.employee_get(path, id)[0]
    resp_status = driver.employee_get(path, id)[1]
    
    # compare values

    assert len(resp_api_json) > 0
    assert resp_status == 200

# Негативная проверка (несуществующий ID)
@pytest.mark.xfail() 
def test_invalid_get_workers_list():
    path = '?company='
    id = 190000
    resp_status = driver.employee_get(path, id)[1]
    assert resp_status == 200

#-----------------------------------------------------------


# Создание записи нового сотрудника
# Позитивная проверка
def test_valid_create_new_note():
    company_id = 277
    first_name = "Dart"
    last_name = "Waider"
    middle_name = "Sith"
    phone = "87776665544"
    url = "www.StarWars.com"

    nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url)
    assert nem_worker[1]== 201

#  Негативная проверка. Неформатный JSON 
@pytest.mark.xfail()  
def test_invalid_create_new_note():
    company_id = 277
    first_name = "Dart"
    last_name = "Waider"
    middle_name = "Sith"
    phone = "87776665544"
    url = "www.StarWars.com"
    godzilla = "Godzilla"
    count = 19955
    
    nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url, godzilla, count)
    assert nem_worker[1]== 201   

#  Негативная проверка. Несуществующий ID
@pytest.mark.xfail()  
def test_invalid_create_new_note_2():
    company_id = 199885

    first_name = "Dart"
    last_name = "Waider"
    middle_name = "Sith"
    phone = "87776665544"
    url = "www.StarWars.com"

    nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url)
    assert nem_worker[1]== 201
    
#-----------------------------------------------------------------------

# Запрос новой записи о сотруднике
#
# Позитивная проверка  \\any_get(self, id, path='')
def test_valid_check_note_new_worker():
    path = '/'
    new_id = 251
    resp_id = driver.employee_get(path, new_id)[0]["id"]
    resp_status = driver.employee_get(path, new_id)[1]
    assert resp_id == new_id
    assert resp_status == 200

# Негативная проверка. Несоответствующий статус.
@pytest.mark.xfail() 
def test_invalid_check_note_new_worker():
    path = '/'
    new_id = 251
    resp_id = driver.employee_get(path, new_id)[0]["id"]
    resp_status = driver.employee_get(path, new_id)[1]
    assert resp_id == new_id
    assert resp_status == 201

# Негативная проверка. Запрос по несуществующему ID
@pytest.mark.xfail() 
def test_invalid_check_note_new_worker_2():
    path = '/'
    new_id = 9887
    resp_status = driver.employee_get(path, new_id)[1]
    assert resp_status == 200    
#-------------------------------------------------------------


# Редактирование существующей записи о сотруднике
#
# Позитивная проверка
def test_valid_change_worker_note():
    new_id = 258
    lastName = "Скайуокер"
    email= "Jabba_hat@tatuin.ru"
    url = "https://Pandora.com"
    isActive = True

    resp = driver. employee_patch(new_id, lastName, email, url, isActive)
    resp_status = resp[1]
    resp_id = resp[0]["id"]
    resp_email = resp[0]["email"]
    resp_url = resp[0]["url"]
    resp_isActive = resp[0]["isActive"]

    assert resp_id == new_id
    assert resp_email == email
    assert resp_url == url
    assert resp_isActive == isActive
    assert resp_status == 200
    
# Негативная проверка. Неформатный JSON
@pytest.mark.xfail() 
def test_invalid_change_worker_note():
    new_id = 258
    lastName = "Скайуокер"
    email= "Jabba_hat@tatuin.ru"
    url = "https://Pandora.com"
    isActive = True
    title = "Alien vs Predator"
    data = 1995

    resp = driver. employee_patch(new_id, lastName, email, url, isActive, title, data)
    resp_status = resp[1]
    # resp_id = resp[0]["id"]
    # resp_email = resp[0]["email"]
    # resp_url = resp[0]["url"]
    # resp_isActive = resp[0]["isActive"]

    # assert resp_id == new_id
    # assert resp_email == email
    # assert resp_url == url
    # assert resp_isActive == isActive
    assert resp_status == 200

# Негативная проверка. Недопустимое значение для ключа "isActive"
@pytest.mark.xfail() 
def test_invalid_change_worker_note_2():
    new_id = 258
    lastName = "Скайуокер"
    email= "Jabba_hat@tatuin.ru"
    url = "https://Pandora.com"
    isActive = "Thank you very much"

    resp = driver. employee_patch(new_id, lastName, email, url, isActive)
    resp_status = resp[1]
    resp_id = resp[0]["id"]
    resp_email = resp[0]["email"]
    resp_url = resp[0]["url"]
    resp_isActive = resp[0]["isActive"]

    assert resp_id == new_id
    assert resp_email == email
    assert resp_url == url
    assert resp_isActive == isActive
    assert resp_status == 200


# Негативная проверка. Несуществующий ID работника
@pytest.mark.xfail() 
def test_invalid_change_worker_note_3():
    new_id = 996633
    lastName = "Скайуокер"
    email= "Jabba_hat@tatuin.ru"
    url = "https://Pandora.com"
    isActive = True

    resp = driver. employee_patch(new_id, lastName, email, url, isActive)
    resp_status = resp[1]
    # resp_id = resp[0]["id"]
    # resp_email = resp[0]["email"]
    # resp_url = resp[0]["url"]
    # resp_isActive = resp[0]["isActive"]

    # assert resp_id == new_id
    # assert resp_email == email
    # assert resp_url == url
    # assert resp_isActive == isActive
    assert resp_status == 200