import datetime
import json
import os
import mysql.connector
from ..database.db import CONNECTION_PARAMS

class Sender:

    def __init__(self, request) :
        self.teacher_id = request.get("id")
        
    def __EncodeData(self, data):
        assert isinstance(data, dict)
        
        return json.dumps(data).replace('"',"'")

    def SendData(self, data):

        encoded_data = self.__EncodeData(data)

        with mysql.connector.connect(**CONNECTION_PARAMS) as db:
            
            db.autocommit = True
            
            with db.cursor() as cursor:
                cursor.execute(f"""
                    INSERT INTO PendingResponse(teacher_id, date, response)
                                VALUES ({self.teacher_id}, "{datetime.date.today()}", "{encoded_data}")
                """)


        # Print result into the log file
    
        ROOT_DIR = os.path.dirname( os.path.dirname(__file__) )
        LOGS_DIR = os.path.join(ROOT_DIR, 'logs')
        if not os.path.exists( LOGS_DIR ):
            os.makedirs(LOGS_DIR)
            
        with open( os.path.join(LOGS_DIR, 'log.txt') ) as log_file:
            log_file.write(encoded_data)
    