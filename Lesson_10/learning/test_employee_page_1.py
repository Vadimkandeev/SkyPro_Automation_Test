from EmployeeClass import EmployeeClass
import pytest
from Table_employee_class import Table_employee_class

driver = EmployeeClass('https://x-clients-be.onrender.com/employee')
db = Table_employee_class("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")
                        
# Запрос всего списка сотрудников 
# "select * from employee e where \"companyId\" =:company_id"
# Позитивная проверка

def test_positive_get_workers_list():
    #  Запрашиваем список сотрудников через API
    request_text = "select * from employee e where \"companyId\" =:curent_id"
    path = '?company='
    id = 3
    resp_api_json = driver.employee_get(path, id)[0]
    resp_status = driver.employee_get(path, id)[1]
    # Запрашивем список сотрудников черед базу данных
    db_result = db.get_any_db_request(id, request_text)
    # сравниваем результаты запросов
    assert len(resp_api_json) == len(db_result)
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
    request_text = "select first_name, last_name, middle_name, phone, avatar_url, \"isActive\", id from employee e where id = :curent_id "
    api_resp_first_name = "Dart"
    api_resp_last_name = "Waider"
    api_resp_middle_name = "Sith"
    api_resp_phone = "87776665544"
    api_resp_url = "www.StarWars.com"
    api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
    api_resp_new_worker_id = api_resp_new_worker[0]['id'] # записываем новый id в переменную, чтобы создать запрос в БД
    # Делаем запрос вновь созданной записи из БД  
    new_db_resp = db.get_any_db_request(api_resp_new_worker_id, request_text)
    
    # Делаем сверку отправленных через API значений и ответа полученного из БД
    assert api_resp_new_worker_id == new_db_resp[0]["id"]
    assert api_resp_first_name == new_db_resp[0]["first_name"] 
    assert api_resp_last_name == new_db_resp[0]["last_name"]
    assert api_resp_middle_name == new_db_resp[0]["middle_name"]
    assert api_resp_phone == new_db_resp[0]["phone"]
    assert api_resp_url == new_db_resp[0]["avatar_url"]
    assert api_resp_new_worker[1]== 201

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
# Позитивная проверка  
def test_valid_check_note_new_worker():
    path = '/'
    curent_id = 251
    request_text = "select * from employee e where id = :curent_id "
    resp_status = driver.employee_get(path, curent_id)[1]
    api_resp_id = driver.employee_get(path, curent_id)[0]["id"]
    api_resp_isActive = driver.employee_get(path, curent_id)[0]["isActive"]
    api_resp_first_name = driver.employee_get(path, curent_id)[0]["firstName"]
    api_resp_last_name = driver.employee_get(path, curent_id)[0]["lastName"]
    api_resp_middle_name = driver.employee_get(path, curent_id)[0]["middleName"]
    api_resp_phone = driver.employee_get(path, curent_id)[0]["phone"]
    api_resp_email = driver.employee_get(path, curent_id)[0]["email"]
    api_resp_url = driver.employee_get(path, curent_id)[0]["avatar_url"]
    api_resp_company_id = driver.employee_get(path, curent_id)[0]["companyId"]

    # Делаем запрос в базу данных 
    new_db_resp = db.get_any_db_request(curent_id, request_text)
    
    # Делаем сверку полученных через API значений и ответа полученного из БД
    assert resp_status == 200
    assert api_resp_id == new_db_resp[0]["id"]
    assert api_resp_isActive == new_db_resp[0]["isActive"]
    assert api_resp_first_name == new_db_resp[0]["first_name"] 
    assert api_resp_last_name == new_db_resp[0]["last_name"]
    assert api_resp_middle_name == new_db_resp[0]["middle_name"]
    assert api_resp_phone == new_db_resp[0]["phone"]
    assert api_resp_email == new_db_resp[0]["email"]
    assert api_resp_url == new_db_resp[0]["avatar_url"]
    assert api_resp_company_id == new_db_resp[0]["companyId"]


# Негативная проверка. Несоответствующий статус.
@pytest.mark.xfail() 
def test_invalid_check_note_new_worker():
    path = '/'
    new_id = 251
    api_resp_id = driver.employee_get(path, new_id)[0]["id"]
    api_resp_status = driver.employee_get(path, new_id)[1]
    assert api_resp_id == new_id
    assert api_resp_status == 201

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
    curent_id = 258
    lastName = "Скайуокер"
    email= "Jabba_hat@tatuin.ru"
    url = "https://Pandora.com"
    isActive = True
    request_text = "select * from employee e where id = :curent_id "
    resp = driver. employee_patch(curent_id, lastName, email, url, isActive)
    api_resp_status = resp[1]
    api_resp_id = resp[0]["id"]
    api_resp_email = resp[0]["email"]
    api_resp_url = resp[0]["url"]
    api_resp_isActive = resp[0]["isActive"]

    #  делаем запрос в базу данных
    db_resp = db.get_any_db_request(curent_id, request_text)
    # Сравниваем ответы полученные через API и из БД
    assert api_resp_id == db_resp[0]["id"]
    assert api_resp_email == db_resp[0]["email"]
    assert api_resp_url == db_resp[0]["avatar_url"]
    assert api_resp_isActive == db_resp[0]["isActive"]
    assert api_resp_status == 200
    
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
    assert resp_status == 200