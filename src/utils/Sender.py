import sys
import os
import json

global _DATABASE_NAME_
global _DATABASE_HOST_
global _DATABASE_PORT_
global _USER_
global _PASSWORD_

_USER_ = "SchoolEyes"
_PASSWORD_ = "schooleyes"

_DATABASE_NAME_ = "School_Eyes"
_DATABASE_HOST_ = "localhost"
_DATABASE_PORT_ = 3306

class Sender:

    def __init__(self, request) :
        self.teacher_id = request.get("id")
        

    def SendData(self, data):
        db = connect(host=_DATABASE_HOST_,
                                port=_DATABASE_PORT_,
                                user=_USER_,
                                password=_PASSWORD_,
                                database=_DATABASE_NAME_)

        cursor = db.cursor()

        result = cursor.execute(f"""
            INSERT INTO PendingResponse(teacher_id, date, response)
                        VALUES ({self.teacher_id}, NOW(), {json.dumps(data)})
        """)

        print(result)

    