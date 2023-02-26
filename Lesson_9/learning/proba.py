from sqlalchemy import create_engine
from sqlalchemy.sql import text
db_connection_string = "postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients"



def test_get_db_workers_note():
        db = create_engine(db_connection_string)
        text_res = "select first_name, last_name, middle_name, phone, avatar_url, \"isActive\" from employee e where \"companyId\" = :company_id and id = :new_id "
        sql_statement = text(text_res)
        resp = db.execute(sql_statement, company_id=277, new_id=177, ).fetchall()
        print(resp[0]['id'])


def func():
        my_list = [1, "kldflsdfjls", 'fskldkslv', 255636]
        for i in range(len(my_list)):
                if i < len(my_list):
                        print(my_list[i], ",")
                
func()
#---------------------------------------------
request_text = "sselect * from employee e where id = :worker_id "


def test_valid_check_note_new_worker():
    path = '/'
    new_id = 251
    resp_id = driver.employee_get(path, new_id)[0]["id"]
    resp_status = driver.employee_get(path, new_id)[1]
    assert resp_id == new_id
    assert resp_status == 200



    new_worker = driver.employee_post(company_id, first_name, last_name, middle_name, phone, url)
    new_worker_id = new_worker[0]['id'] # записываем новый id в переменную, чтобы создать запрос в БД
    # Делаем запрос вновь созданной записи из БД  
    new_db_resp = db.get_note_new_employee(company_id, new_worker_id, request_text)

{
    "id": 667,
    "isActive": true,
    "createDateTime": "2023-02-26T20:04:12.839Z",
    "lastChangedDateTime": "2023-02-26T20:04:12.839Z",
    "firstName": "Дарт",
    "lastName": "Ситхович",
    "middleName": "Вейдер",
    "phone": "89155693658",
    "email": null,
    "avatar_url": "http://DeadStar_Tatuin",
    "companyId": 277
}