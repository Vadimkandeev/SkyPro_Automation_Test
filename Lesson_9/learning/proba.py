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
