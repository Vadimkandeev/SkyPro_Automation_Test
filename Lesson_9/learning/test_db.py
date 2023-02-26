from sqlalchemy import create_engine
from sqlalchemy.sql import text
db_connection_string = "postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients"

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'user'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]

    assert row1[0] == 1
    assert row1['name'] == "Барбершоп 'ЦирюльникЪ'"


def test_select_row1():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 314).fetchall()
    assert len(rows) == 1  
    assert rows[0]["name"] == "name1"


def test_select_row1_with_two_filtres():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"isActive\" = :isActive and id = :id")
    my_params = {
        'id':314,
        'isActive': True
    }
    rows = db.execute(sql_statement, my_params).fetchall()
    assert len(rows) == 1  
    assert rows[0]["name"] == "name"


def test_insert():  
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")  
    rows = db.execute(sql, new_name = 'Papa Carlo')
    1 == 1

def test_update():  
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr  where id = :new_id")  
    rows = db.execute(sql, descr = "new descr", new_id = 162)
    1 == 1


def test_delete():  
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :new_id")  
    rows = db.execute(sql, new_id = 321)
    1 == 1


def test_get_list_employee():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from employee e where \"companyId\" =:company_id")
    rows = db.execute(sql_statement, company_id=3).fetchall()
    #assert len(rows) == 1  
    #assert rows[0]["name"] == "name1"

def test_get_db_workers_note():
        db = create_engine(db_connection_string)
        text_res = "select first_name, last_name, middle_name, phone, avatar_url, \"isActive\" from employee e where \"companyId\" = :company_id and id = :new_id "
        sql_statement = text(text_res)
        resp = db.execute(sql_statement, company_id=277, new_id=177, ).fetchall()
        

        return resp

def clearly_not_pass_by_value():
    l = [1, 2, 3]
    print(l)


clearly_not_pass_by_value()
    



