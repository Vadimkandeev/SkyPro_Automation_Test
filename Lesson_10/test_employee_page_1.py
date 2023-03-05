import allure
import pytest
from EmployeeClass import EmployeeClass
from Table_employee_class import Table_employee_class
from faker import Faker


driver = EmployeeClass('https://x-clients-be.onrender.com/employee')
db = Table_employee_class("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")
fake = Faker()                       
# Запрос всего списка сотрудников 
# 
# Позитивная проверка
@allure.description("ПОлучить список сотрудников и БД и при помощи запроса чарез  API и сравнить полученные данные")
@allure.feature("Позитивная проверка")
@allure.title("Запрос списка сотрудников.")
@allure.severity("Critical")
def test_positive_get_workers_list():
    with allure.step("Получить список сотрудников через API"):
        with allure.step("Добавить данные дла запроса"):
            path = '?company='
            name = fake.name()
            descr = fake.text(20)
            id = driver.create_company(name, descr)
        with allure.step("Сделать запрос через API"):
            resp_api_json = driver.employee_get(path, id)[0]
            resp_status = driver.employee_get(path, id)[1]
    with allure.step("Получить список сотрудников через БД"):
        with allure.step("Сформировать запрос БД"):
            request_text = "select * from employee e where \"companyId\" =:curent_id"
        with allure.step("Сделать запрос в БД"):
            db_result = db.get_any_db_request(id, request_text)
    
    with allure.step("сравнить результаты запросов API и БД"):
        assert len(resp_api_json) == len(db_result)
        assert resp_status == 200
    

# Негативная проверка (несуществующий ID)
@allure.description("Сформировать запрос списка вех сотрудников компании с несуществующим ID по API и проверить статус код возвращаемого ответа")
@allure.feature("Негативная проверка")
@allure.title("Запрос списка сотрудников.")
@allure.severity("Critical")
@pytest.mark.xfail() 
def test_invalid_get_workers_list():
    with allure.step("Сформировать невалидные данные для запроса по API"):
        path = '?company='
        id = 190000
        resp_status = driver.employee_get(path, id)[1]
    with allure.step("Спроверить статус ответа"):    
        assert resp_status == 200

#-----------------------------------------------------------


# Создание записи нового сотрудника
# Позитивная проверка
@allure.description("Создать новую компанию, в этой компании создать запись о новом сотруднике. Сделать запрос о создании \
                    по  API и через БД. Сравнить результаты возвращаемых ответов")
@allure.feature("Позитивная проверка")
@allure.title("Создание нового сотрудника.")
@allure.severity("Critical")
def test_valid_create_new_note():
    with allure.step("Получить данные по API для создания новой записи о сотруднике"):
        with allure.step("Сгенерировать данные для запроса по API"):
            company_id = driver.create_company(fake.name(), fake.text(20))
            api_resp_first_name = fake.first_name()
            api_resp_last_name = fake.last_name()
            api_resp_middle_name = fake.first_name()
            api_resp_phone = "2222222222"
            api_resp_url = fake.url()
        with allure.step("Отправить запрос по API"):
            api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
        with allure.step("Из полученного ответа выделить id"):    
            api_resp_new_worker_id = api_resp_new_worker[0]['id'] # записываем новый id в переменную, чтобы создать запрос в БД
    # Делаем запрос вновь созданной записи из БД 
    with allure.step("Получить данные из БД"): 
        with allure.step("формировать запрос в БД"): 
            request_text = "select first_name, last_name, middle_name, phone, avatar_url, \"isActive\", id from employee e where id = :curent_id "  
        with allure.step("Отправить запрос в БД"): 
            new_db_resp = db.get_any_db_request(api_resp_new_worker_id, request_text)
    
    # Делаем сверку отправленных через API значений и ответа полученного из БД
    with allure.step("Провести сверку данных, полученных по API и из БД"): 
        assert api_resp_new_worker_id == new_db_resp[0]["id"]
        assert api_resp_first_name == new_db_resp[0]["first_name"] 
        assert api_resp_last_name == new_db_resp[0]["last_name"]
        assert api_resp_middle_name == new_db_resp[0]["middle_name"]
        assert api_resp_phone == new_db_resp[0]["phone"]
        assert api_resp_url == new_db_resp[0]["avatar_url"]
        assert api_resp_new_worker[1]== 201

#  Негативная проверка. Неформатный JSON 
@allure.description("Создать новую компанию, в этой компании создать запись о новом сотруднике. Сделать запрос о создании \
                    по  API и через БД. В запросе по API намерено отправить невалидные данные. \
                    Сравнить результаты возвращаемых ответов. Проверить статус-код, возвращаемый по API")
@allure.feature("Негативная проверка")
@allure.title("Создание нового сотрудника.")
@allure.severity("Critical") 
@pytest.mark.xfail() 
def test_invalid_create_new_note():
    with allure.step("Сформировать невалидные значения для запроса"):
        company_id = driver.create_company(fake.name(), fake.text(20))
        first_name = fake.first_name()
        last_name = fake.last_name()
        middle_name = fake.first_name()
        phone = "2222222222222"
        url = fake.url()
        godzilla = fake.text(10)
        date = fake.date_time()
    with allure.step("Сделать запрос по API"):
        driver.employee_post(company_id, first_name, last_name, middle_name, phone, url, godzilla, date)
        nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url, godzilla, date)
    with allure.step("Запросить статус ответа"):    
        assert nem_worker[1]== 201   

#  Негативная проверка. Несуществующий ID
@allure.description("Создать запись о новом сотруднике. Сделать запрос о создании записи \
                    по  API и через БД. В запросе по API намерено указать невалидные данные. \
                    Сравнить результаты возвращаемых ответов. Проверить статус-код, возвращаемый по API")
@allure.feature("Негативная проверка")
@allure.title("Создание нового сотрудника.")
@allure.severity("Critical") 
@pytest.mark.xfail()  
def test_invalid_create_new_note_2():
    with allure.step("Задать невалидные данные для запроса"):
        company_id = 99999999999999999 #driver.create_company(fake.name(), fake.text(20))
        first_name = fake.first_name()
        last_name = fake.last_name()
        middle_name = fake.first_name()
        phone = fake.phone_number()
        url = fake.url()
    with allure.step("Отправить запрос по API"):
        nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url)
    with allure.step("Сравнить статус ответа с ожидаемым"):
        assert nem_worker[1]== 201    
#-----------------------------------------------------------------------

# Запрос новой записи о сотруднике
#
# Позитивная проверка
@allure.description("Создать новую компанию. В этой компании создать новую запись о сотруднике. Запросить информацию о сотруднике \
                    по  API и через БД. Сравнить результаты возвращаемых ответов. Проверить статус-код, возвращаемый по API")
@allure.feature("Позитивная проверка")
@allure.title("Получение записи о сотруднике")
@allure.severity("Critical") 
def test_valid_check_note_new_worker():
    with allure.step("Получить данные из API"):  
        with allure.step("Перед получением записи о сотруднике создать её"):
            company_id = driver.create_company(fake.name(), fake.text(20))
        with allure.step("Задать данные для запроса"):
            api_resp_first_name = fake.first_name()
            api_resp_last_name = fake.last_name()
            api_resp_middle_name = fake.first_name()
            api_resp_phone = "22222222222222"
            api_resp_url = fake.url() 
        with allure.step("Сформировать запрос по API"): 
            api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
        with allure.step("ПОлучить данные из API"): 
            curent_id =  api_resp_new_worker[0]['id']
            path = '/'
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
    with allure.step("ПОлучить данные из БД"): 
        with allure.step("Сформировать запрос с БД"): 
            request_text = "select * from employee e where id = :curent_id "
        with allure.step("Отправить запросвс БД"): 
            new_db_resp = db.get_any_db_request(curent_id, request_text)
    
    with allure.step("Сравнить результаты запросов по API с данными из БД"): 
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
@allure.description("Создать новую компанию. В этой компании создать новую запись о сотруднике. Запросить информацию о сотруднике \
                    по  API и через БД. Провести проверку с неверным статус-кодом, возвращаемый по API")
@allure.feature("Негативная проверка")
@allure.title("Получение записи о сотруднике")
@allure.severity("Major") 
@pytest.mark.xfail() 
def test_invalid_check_note_new_worker():
    with allure.step("Получить данные из API"):  
        with allure.step("Перед получением записи о сотруднике создать её"):
            company_id = driver.create_company(fake.name(), fake.text(20))
            api_resp_first_name = fake.first_name()
            api_resp_last_name = fake.last_name()
            api_resp_middle_name = fake.first_name()
            api_resp_phone = "222222222222"
            api_resp_url = fake.url()    
            api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)     
            new_id =  api_resp_new_worker[0]['id']
        with allure.step("Отправить запрос по API. ПОлучить данные"):
            path = '/'
            api_resp_id = driver.employee_get(path, new_id)[0]["id"]
            api_resp_status = driver.employee_get(path, new_id)[1]
    with allure.step("Проверить данные из API"):
        assert api_resp_id == new_id
        assert api_resp_status == 201

# Негативная проверка. Запрос по несуществующему ID
@allure.description("Сформировать данные для запроса с несуществующим id. Запросить информацию о сотруднике \
                    по  API. Провести проверку статус-кода, возвращаемого по API")
@allure.feature("Негативная проверка")
@allure.title("Получение записи о сотруднике")
@allure.severity("Major") 
@pytest.mark.xfail() 
def test_invalid_check_note_new_worker_2():
    with allure.step("Сформировать данные для запроса по API"):
        path = '/'
        new_id = 9887
    with allure.step("Получить данные из API"):
        resp_status = driver.employee_get(path, new_id)[1]
    with allure.step("ПРовести сравнение ответа"):
        assert resp_status == 200    
#-------------------------------------------------------------


# Редактирование существующей записи о сотруднике
#
# Позитивная проверка

@allure.description("Создать новую компанию, создать в ней запись о новом сотруднике . Изменить  информацию о сотруднике \
                    по  API.  Запросить измененные данные о сотруднике через БД. Провести проверку\
                    соответствие данных полученных по API и с БД")
@allure.feature("Позитивная проверка")
@allure.title("Редактирование записи о сотруднике")
@allure.severity("Critical") 
def test_valid_change_worker_note():
    with allure.step("Отправить запрос по API"):
        with allure.step("Перед редактированием записи о сотруднике создать её"):
            company_id = driver.create_company(fake.name(), fake.text(20))
            api_resp_first_name = fake.first_name()
            api_resp_last_name = fake.last_name()
            api_resp_middle_name = fake.first_name()
            api_resp_phone = "222222222222"
            api_resp_url = fake.url()
            api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
            curent_id =  api_resp_new_worker[0]['id']
        with allure.step("Сформировать новые данные для запроса по API"):
            lastName = fake.first_name()
            email= fake.email()
            url = fake.url()
            isActive = True
        with allure.step("Отправить запрос по API"):
            resp = driver. employee_patch(curent_id, lastName, email, url, isActive)
        with allure.step("Получить данные по API"):
            api_resp_status = resp[1]
            api_resp_id = resp[0]["id"]
            api_resp_email = resp[0]["email"]
            api_resp_url = resp[0]["url"]
            api_resp_isActive = resp[0]["isActive"]
    with allure.step("Отправить запрос в БД"):
        with allure.step("Сформировать запрос в БД"):
            request_text = "select * from employee e where id = :curent_id "
        db_resp = db.get_any_db_request(curent_id, request_text)
    with allure.step("Сравнить результаты запроса по API с ответом  с БД"):
        assert api_resp_id == db_resp[0]["id"]
        assert api_resp_email == db_resp[0]["email"]
        assert api_resp_url == db_resp[0]["avatar_url"]
        assert api_resp_isActive == db_resp[0]["isActive"]
        assert api_resp_status == 200


# Негативная проверка. Неформатный JSON    
@allure.description("Создать новую компанию, создать в ней запись о новом сотруднике . Изменить  информацию о сотруднике \
                    по  API. В запросе по API отправить данные с нарушенем формата.  Запросить измененные данные о \
                     сотруднике через БД. Провести проверку возвращаемого статус-кода")
@allure.feature("Негативная проверка")
@allure.title("Редактирование записи о сотруднике")
@allure.severity("Major") 
@pytest.mark.xfail() 
def test_invalid_change_worker_note():
    # Перед редактированием записи о новом сотруднике, создаем запись
    with allure.step("Отправить запрос на изменение записи по API"):
        with allure.step("Перед изменением записи о сотруднике создать её"):
            company_id = driver.create_company(fake.name(), fake.text(20))
            api_resp_first_name = fake.first_name()
            api_resp_last_name = fake.last_name()
            api_resp_middle_name = fake.first_name()
            api_resp_phone = "22222222222"
            api_resp_url = fake.url()
            api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
            new_id =  api_resp_new_worker[0]['id']
        with allure.step("Сформировать данные для изменения записи"):
            lastName = fake.last_name()
            email= fake.email()
            url = fake.url()
            isActive = True
            title = fake.text(20)
            data = fake.date_time()
        with allure.step("ПОлучить ответ по API"):
            resp = driver. employee_patch(new_id, lastName, email, url, isActive, title, data)
    with allure.step("Сравнить результаты ответа по API с ожидаемыми"):
        resp_status = resp[1]
        assert resp_status == 200

# Негативная проверка. Недопустимое значение для ключа "isActive"
@allure.description("Создать новую компанию, создать в ней запись о новом сотруднике . Изменить  информацию о сотруднике \
                    по  API. В запросе по API отправить данные с нарушением формата значения для ключа 'isActive'.  Запросить измененные данные о \
                     сотруднике через БД. Провести проверку возвращаемого тела ответа. Провести проверку возвращаемого статус-кода")
@allure.feature("Негативная проверка")
@allure.title("Редактирование записи о сотруднике")
@allure.severity("Major") 
@pytest.mark.xfail() 
def test_invalid_change_worker_note_2():
    # Перед редактированием записи о новом сотруднике, создаем запись
    with allure.step("Отправить запрос на изменение записи по API"):
        with allure.step("Перед изменением записи о сотруднике создать её"):
            company_id = driver.create_company(fake.name(), fake.text(20))
            api_resp_first_name = fake.first_name()
            api_resp_last_name = fake.last_name()
            api_resp_middle_name = fake.first_name()
            api_resp_phone = "222222222222"
            api_resp_url = fake.url()
            api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
            new_id =  api_resp_new_worker[0]['id']
        with allure.step("Сформировать данные для запроса"):
            lastName = fake.last_name()
            email= fake.email()
            url = fake.url()
            isActive = 3222154
        with allure.step("Получить данные по API"):
            resp = driver. employee_patch(new_id, lastName, email, url, isActive)
            resp_status = resp[1]
            resp_id = resp[0]["id"]
            resp_email = resp[0]["email"]
            resp_url = resp[0]["url"]
            resp_isActive = resp[0]["isActive"]
    with allure.step("Сравнить данные ответа API с ожидаемыми"):
        assert resp_id == new_id
        assert resp_email == email
        assert resp_url == url
        assert resp_isActive == isActive
        assert resp_status == 200


# Негативная проверка. Несуществующий ID работника

@allure.description("Сформировать данные для запроса. В данных для запроса указать несуществующий id. Отправить запрос по  по  API.\
                    Провести проверку возвращаемого тела ответа. Провести проверку возвращаемого статус-кода")
@allure.feature("Негативная проверка")
@allure.title("Редактирование записи о сотруднике")
@allure.severity("Major") 
@pytest.mark.xfail() 
def test_invalid_change_worker_note_3():
    with allure.step("Сформировать данные для запроса API"):
        lastName = fake.last_name()
        email= fake.email()
        url = fake.url()
        isActive = True
        new_id = 99663300124516554
    with allure.step("Отправить по запрос API"):
        resp = driver. employee_patch(new_id, lastName, email, url, isActive)
    with allure.step("ПОлучить ответ API"):
        resp_status = resp[1]
    with allure.step("Сравнить статус ответа с ожидаемым"):
        assert resp_status == 200
