from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Table_employee_class:

 
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
 
    # Так как все запросы происходят по одному шаблону, то достаточно всего одного метода
    # Непосредственно, SQL запрос к БД и переменные передаются как параметры метода
    def get_any_db_request(self, curent_id, request_text):
        sql_statement = text(request_text)
        return self.db.execute(sql_statement, curent_id=curent_id).fetchall()
   

    
    