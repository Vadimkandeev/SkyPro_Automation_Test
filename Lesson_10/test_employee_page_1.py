import allure
import pytest
from EmployeeClass import EmployeeClass
from Table_employee_class import Table_employee_class

driver = EmployeeClass('https://x-clients-be.onrender.com/employee')
db = Table_employee_class("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")
                        
# Запрос всего списка сотрудников 
# 
# Позитивная проверка
@allure.id("Vadim kandeev. Test_1")
@allure.story(" Получение списка сотрудников компании")
@allure.title("Запрос списка сотрудников. Позитивная проверка")
def test_positive_get_workers_list():
    with allure("Получить список сотрудников через API"):
        #  Запрашиваем список сотрудников через API
        with allure("Добавить данные дла запроса"):
            request_text = "select * from employee e where \"companyId\" =:curent_id"
            path = '?company='
            id = 1357
        with allure("Сделать запрос через API"):
            resp_api_json = driver.employee_get(path, id)[0]
            resp_status = driver.employee_get(path, id)[1]
    with allure("Получить список сотрудников через БД"):
        # Запрашивем список сотрудников черед базу данных
        db_result = db.get_any_db_request(id, request_text)
    with allure("Сравнить результаты запросов"):
        # сравниваем результаты запросов
        assert len(resp_api_json) == len(db_result)
        assert resp_status == 200
    

# Негативная проверка (несуществующий ID)
@allure.story(" Получение списка сотрудников компании")
@allure.id("Vadim kandeev. Test_2")
@allure.title("Запрос списка сотрудников. Негативная проверка (несуществующий ID)")
@pytest.mark.xfail() 
def test_invalid_get_workers_list():
    with allure("Дабавить невалидные данные"):
        path = '?company='
        id = 190000
        resp_status = driver.employee_get(path, id)[1]
    with allure("Запросить статус ответа"):    
        assert resp_status == 200

#-----------------------------------------------------------


# Создание записи нового сотрудника
# Позитивная проверка
@allure.id("Vadim kandeev. Test_3")
@allure.story("Создание записи нового сотрудника")
@allure.title("Создание записи нового сотрудника. Позитивня проверка")
def test_valid_create_new_note():
    
    with allure("Создать запись нового сотрудника"):
        with allure("Сгененерировать данные нового сотрудника"):
            company_id = 1357
            request_text = "select first_name, last_name, middle_name, phone, avatar_url, \"isActive\", id from employee e where id = :curent_id "
            api_resp_first_name = "Dart"
            api_resp_last_name = "Waider"
            api_resp_middle_name = "Sith"
            api_resp_phone = "87776665544"
            api_resp_url = "www.StarWars.com"
            api_resp_new_worker = driver.employee_post(company_id, api_resp_first_name, api_resp_last_name, api_resp_middle_name, api_resp_phone, api_resp_url)
            api_resp_new_worker_id = api_resp_new_worker[0]['id'] # записываем новый id в переменную, чтобы создать запрос в БД
        with allure("Делаем запрос с БД"):
            # Делаем запрос вновь созданной записи из БД  
            new_db_resp = db.get_any_db_request(api_resp_new_worker_id, request_text)
    
    with allure("Сделать сверку отправленных через API значений и ответа полученного из БД"):
        # Делаем сверку отправленных через API значений и ответа полученного из БД
        assert api_resp_new_worker_id == new_db_resp[0]["id"]
        assert api_resp_first_name == new_db_resp[0]["first_name"] 
        assert api_resp_last_name == new_db_resp[0]["last_name"]
        assert api_resp_middle_name == new_db_resp[0]["middle_name"]
        assert api_resp_phone == new_db_resp[0]["phone"]
        assert api_resp_url == new_db_resp[0]["avatar_url"]
        assert api_resp_new_worker[1]== 201

#  Негативная проверка. Неформатный JSON 
@allure.story("Создание записи нового сотрудника")
@allure.id("Vadim kandeev. Test_4")
@pytest.mark.xfail()  
@allure.title("Создание записи нового струдника. Негативная проверка. Неформатный JSON ")
def test_invalid_create_new_note():
    with allure("Задать невалидные данные для запроса"):
        company_id = 1357
        first_name = "Dart"
        last_name = "Waider"
        middle_name = "Sith"
        phone = "87776665544"
        url = "www.StarWars.com"
        godzilla = "Godzilla"
        count = 19955
    with allure("Сделать запрос по API"):
        nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url, godzilla, count)
    with allure("Запросить статус ответа"):
        assert nem_worker[1]== 201   

#  Негативная проверка. Несуществующий ID
@allure.story("Создание записи нового сотрудника")
@allure.id("Vadim kandeev. Test_5")
@pytest.mark.xfail() 
@allure.title("Создание записи нового струдника. Негативная проверка. Несуществующий ID") 
def test_invalid_create_new_note_2():
    with allure("Задать невалидные данные для запроса"):
        company_id = 199885
        first_name = "Dart"
        last_name = "Waider"
        middle_name = "Sith"
        phone = "87776665544"
        url = "www.StarWars.com"
    with allure("Сделать запрос по API"):
        nem_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url)
    with allure("Запросить стату ответа"):
        assert nem_worker[1]== 201
    
#-----------------------------------------------------------------------

# Запрос новой записи о сотруднике
#
# Позитивная проверка  
@allure.id("Vadim kandeev. Test_6")
@allure.story(" Получение новой записи о сотруднике")
@allure.title("Запрос записи нового струдника. Позитивная проверка.")
def test_valid_check_note_new_worker():
    with allure("Получить данные из API"):  
        with allure("Задать данные для запроса"):
            path = '/'
            curent_id = 127
        with allure("Получить ответ через API"):    
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
    
    with allure("Получить данные из БД"):  
        with allure("Сформировать запрос к БД"):    
            request_text = "select * from employee e where id = :curent_id "
    
        with allure("Сделать запрос созданной записи из БД"):
            # Делаем запрос в базу данных 
            new_db_resp = db.get_any_db_request(curent_id, request_text)

    with allure("Сделать сверку полученных через API значений и ответа полученного из БД"):
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
@allure.id("Vadim kandeev. Test_7")
@allure.story(" Получение новой записи о сотруднике")
@allure.title("Запрос записи нового струдника. Негативная проверка. Несоответствующий статус")
@pytest.mark.xfail() 
def test_invalid_check_note_new_worker():
    with allure("Сформировать данные для запроса по API"):
        path = '/'
        new_id = 251
    with allure("Сделать запрос созданной записи по API"):
        api_resp_id = driver.employee_get(path, new_id)[0]["id"]
        api_resp_status = driver.employee_get(path, new_id)[1]
    with allure("Сравнить запрос и ответ"):
        assert api_resp_id == new_id
        assert api_resp_status == 201

# Негативная проверка. Запрос по несуществующему ID
@allure.id("Vadim kandeev. Test_8")
@allure.story(" Получение новой записи о сотруднике")
@allure.title("Запрос записи нового струдника. Негативная проверка. Запрос по несуществующему ID")
@pytest.mark.xfail() 
def test_invalid_check_note_new_worker_2():
    with allure("Сформировать невалидные данные для запроса по API"):
        path = '/'
        new_id = 9887
    with allure("Отправить запрос по API"):
        resp_status = driver.employee_get(path, new_id)[1]
    with allure("Запросить статус ответа"):    
        assert resp_status == 200    
#-------------------------------------------------------------


# Редактирование существующей записи о сотруднике
#
# Позитивная проверка
@allure.id("Vadim kandeev. Test_9")
@allure.story("Редактирование чуществующей записи о сотруднике")
@allure.title("Редактирование существующей записи о сотруднике. Позитивная проверка.")
def test_valid_change_worker_note():
    with allure("Редактирование существующей записи о сотруднике"):
        with allure("Сформировать данные для запроса по API"):
            curent_id = 127
        lastName = "Скайуокер"
        email= "Jabba_hat@tatuin.ru"
        url = "https://Pandora.com"
        isActive = True
        
        with allure("Сформировать запрос по API"):
            resp = driver. employee_patch(curent_id, lastName, email, url, isActive)
        with allure("Получить данные с API"):
            api_resp_status = resp[1]
            api_resp_id = resp[0]["id"]
            api_resp_email = resp[0]["email"]
            api_resp_url = resp[0]["url"]
            api_resp_isActive = resp[0]["isActive"]
    
        with allure("Сформировать запрос для БД"):
            request_text = "select * from employee e where id = :curent_id "

        with allure("Сделать запрос созданной записи из БД"): 
            #  делаем запрос в базу данных
            db_resp = db.get_any_db_request(curent_id, request_text)

        with allure("Сравнить ответы полученные через API и из БД"):    
            # Сравниваем ответы полученные через API и из БД
            assert api_resp_id == db_resp[0]["id"]
            assert api_resp_email == db_resp[0]["email"]
            assert api_resp_url == db_resp[0]["avatar_url"]
            assert api_resp_isActive == db_resp[0]["isActive"]
            assert api_resp_status == 200
    
# Негативная проверка. Неформатный JSON
@allure.id("Vadim kandeev. Test_10")
@allure.story("Редактирование чуществующей записи о сотруднике")
@allure.title("Редактирование существующей записи о сотруднике. Негативная проверка. Неформатный JSON")
@pytest.mark.xfail() 
def test_invalid_change_worker_note():
    with allure("Негативняа проверка Неформатный JSON"):  
         with allure("формирование данных для запроса"):
            new_id = 127
            lastName = "Скайуокер"
            email= "Jabba_hat@tatuin.ru"
            url = "https://Pandora.com"
            isActive = True
            title = "Alien vs Predator"
            data = 1995
         with allure("Отправка запроса по API"):
            resp = driver. employee_patch(new_id, lastName, email, url, isActive, title, data)
            resp_status = resp[1]
         with allure("Сравнение статуса ответа с ожидаемым"):   
            assert resp_status == 200

# Негативная проверка. Недопустимое значение для ключа "isActive"
@allure.id("Vadim kandeev. Test_11")
@allure.story("Редактирование чуществующей записи о сотруднике")
@allure.title("Редактирование существующей записи о сотруднике. Негативная проверка. Недопустимое значение для ключа 'isActive'")
@pytest.mark.xfail() 
def test_invalid_change_worker_note_2():
    with allure("Негативняа проверка. Недопустимое значение для ключа 'isActive'"):  
        with allure("Сформировать данные для запроса"):
            new_id = 127
            lastName = "Скайуокер"
            email= "Jabba_hat@tatuin.ru"
            url = "https://Pandora.com"
            isActive = "Thank you very much"
        with allure("Отправить запрос для изменения существующей записи"):
            resp = driver. employee_patch(new_id, lastName, email, url, isActive)
        with allure("Получить ответ по API"):   
            resp_status = resp[1]
            resp_id = resp[0]["id"]
            resp_email = resp[0]["email"]
            resp_url = resp[0]["url"]
            resp_isActive = resp[0]["isActive"]
        with allure("Сравнить результаты ответа с данными из запроса"):
            assert resp_id == new_id
            assert resp_email == email
            assert resp_url == url
            assert resp_isActive == isActive
            assert resp_status == 200


# Негативная проверка. Несуществующий ID работника
@allure.id("Vadim kandeev. Test_12")
@allure.story("Редактирование чуществующей записи о сотруднике")
@allure.title("Редактирование существующей записи о сотруднике. Негативная проверка. Несуществующий ID работника")
@pytest.mark.xfail() 
def test_invalid_change_worker_note_3():
    with allure("Негативняа проверка. Несуществующий ID работника"):
        with allure("Сыормировать данные для запроса"):
            new_id = 996633
            lastName = "Скайуокер"
            email= "Jabba_hat@tatuin.ru"
            url = "https://Pandora.com"
            isActive = True
        with allure("Отправить запрос по API"):
            resp = driver. employee_patch(new_id, lastName, email, url, isActive)
        with allure("Получить ответ по API"):
            resp_status = resp[1]
        with allure("Сравнить ответ по API с данными запроса"):
            assert resp_status == 200