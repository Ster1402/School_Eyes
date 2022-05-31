import datetime
import json
import mysql.connector
from ..database.db import CONNECTION_PARAMS

class Sender:

    def __init__(self, request) :
        self.teacher_id = request.get("id")
        
    def __EncodeData(self, data):
        assert isinstance(data, dict)
        
        return json.dumps(data).replace('"',"'")

    def SendData(self, data):
        
        with mysql.connector.connect(**CONNECTION_PARAMS) as db:
            
            db.autocommit = True

            with db.cursor() as cursor:
                cursor.execute(f"""
                    INSERT INTO PendingResponse(teacher_id, date, response)
                                VALUES ({self.teacher_id}, "{datetime.date.today()}", "{self.__EncodeData(data)}")
                """)


    