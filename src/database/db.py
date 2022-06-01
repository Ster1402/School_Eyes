import hashlib
import json
import sqlite3
import os
from unittest import result
import face_recognition as fr

from src.utils.NumpyArrayEncoder import NumpyArrayEncoder

global __ROOT_PATH
__ROOT_PATH = os.path.dirname( os.path.dirname(os.path.abspath(__file__)) )

global _DATABASE_PATH_
_DATABASE_PATH_ = os.path.join( __ROOT_PATH,
                               "database/"
                               "SchoolEyesDB.db" )

"""
    The ID_Generator class help us dynamically
    generate id for a new instance. Because AUTO_INCREMENT
    don't work well in sqlite.

    Usage : 
        1- Declare an instance : 
            ex = student_id = ID_Generator("Student")
        2- Access the id property to get the next id to use:
            ex = INSERT INTO Student VALUES
                    ({student_id.id}, "name", "surname"),
                    ({student_id.id}, "name", "surname"),
                    ({student_id.id}, "name", "surname")
"""
class ID_Generator:

    def __init__(self, table_name: str) -> None:
        self.table_name: str = table_name
        self._id: int = DB.getLastID(table_name=self.table_name)

    @property  
    def id(self):
        self._id += 1
        return self._id

    @id.setter
    def setId(self, value):
        raise ValueError("Don't hardcode the row id!")

class DB:
    __DB_IS_CREATE__: bool = False

    def __init__(self, db_path: str =_DATABASE_PATH_):
        assert isinstance(db_path, str)

        self.db_path = db_path
        self.db_connection = self._connectDB(self.db_path)
        self.cursor = self._getCursor()
        
        if not self.__DB_IS_CREATE__:
            self.createDatabase()
            self.__initAdmin()

            self.__DB_IS_CREATE__ = True

    def _connectDB(self, db_path: str =_DATABASE_PATH_):
        assert isinstance(db_path, str)
        return sqlite3.connect(db_path)

    def _commitChange(self):
        self.db_connection.commit()

    def closeDB(self):
        self.db_connection.close()

    def _getCursor(self):
        return self.db_connection.cursor()

    @staticmethod
    def executeScript_(query: str) -> None:
        print("[Static] executeQuery")
        
        con = sqlite3.connect(_DATABASE_PATH_)
        cursor = con.cursor()
        cursor.execute(query)
        cursor.close()
        con.commit()
        con.close()

    def executeScript(self, query: str) -> None:
        print("[Local] executeQuery")

        self.cursor.executescript(query)
        self._commitChange()


    @staticmethod
    def executeQuery_(query: str):
        print("[Static] executeQuery")
        
        con = sqlite3.connect(_DATABASE_PATH_)
        cursor = con.cursor()
        response = cursor.execute(query)\
                       .fetchall()
        cursor.close()
        con.commit()
        con.close()

        return response

    def executeQuery(self, query: str):
        print("[Local] executeQuery")

        cursor = self.cursor.execute(query)        
        response = cursor.fetchall()
        self._commitChange()

        return response

    #Last id of the table
    @staticmethod
    def getLastID(table_name: str) -> int:
        con = sqlite3.connect(_DATABASE_PATH_)
        cursor = con.cursor()
        result = cursor.execute(f"SELECT MAX(id) as id FROM {table_name}")\
                       .fetchone()
        cursor.close()
        con.close()

        if not result[0]:
            return 0
        
        return result[0]


    #Count numbers of entries 
    @staticmethod
    def count(table_name: str):
        con = sqlite3.connect(_DATABASE_PATH_)
        cursor = con.cursor()
        result = cursor.execute(f"SELECT * FROM {table_name}")\
                       .fetchall()
        cursor.close()
        con.close()
        return len(result)

    def createDatabase(self):

        #Create DB file if not exist
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w"):
                pass

        #Create table in db if not exist
        create_tables_query = """
            CREATE TABLE IF NOT EXISTS Admin(
                id INT AUTO_INCREMENT NOT NULL, 
                login VARCHAR(40) UNIQUE, 
                password VARCHAR(255) NOT NULL,
                status VARCHAR(15) DEFAULT "disconnected",
                PRIMARY KEY(id) 
            );

            CREATE TABLE IF NOT EXISTS Discipline(
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(30),
                PRIMARY KEY(id)
            );

            CREATE TABLE IF NOT EXISTS Axe(
                id INT AUTO_INCREMENT NOT NULL,
                discipline_id INT NOT NULL,
                name VARCHAR(20),
                PRIMARY KEY(id),
                FOREIGN KEY(discipline_id) REFERENCES Discipline(id)
            );

            CREATE TABLE IF NOT EXISTS Student(
                id INT AUTO_INCREMENT NOT NULL,
                axe_id INT NOT NULL,
                name VARCHAR(40) NOT NULL,
                surname VARCHAR(40),
                register_number VARCHAR(10) UNIQUE,
                level INT,
                PRIMARY KEY(id),
                FOREIGN KEY(axe_id) REFERENCES Axe(id)
            );
            
            CREATE TABLE IF NOT EXISTS Picture(
                id INT AUTO_INCREMENT NOT NULL,
                student_id INT NOT NULL,
                path VARCHAR(255) NOT NULL UNIQUE,
                face_encoding TEXT NOT NULL,
                PRIMARY KEY(id),
                FOREIGN KEY(student_id) REFERENCES Student(id)
            );
        """

        #Execute query
        self.executeScript(create_tables_query)

    def cleanDatabase(self):
        self.__DB_IS_CREATE__ = False

        drop_tables_query = """
            DROP TABLE IF EXISTS Admin;
            DROP TABLE IF EXISTS Picture;
            DROP TABLE IF EXISTS Student;
            DROP TABLE IF EXISTS Axe;
            DROP TABLE IF EXISTS Discipline;
        """

        self.executeScript(drop_tables_query)

    def getAdmins(self):
        find_admin = "SELECT * FROM Admin"
        admins = self.executeQuery(find_admin)

        return admins 

    def __initAdmin(self):

        if not self.getAdmins():
            
            sterdevs_default_password = hashlib.md5(b"sterdevs").hexdigest()
            esprit_default_password = hashlib.md5(b"esprit@@@").hexdigest()
            admin_default_password = hashlib.md5(b"admin").hexdigest()

            admin_id = ID_Generator("Admin")
            
            create_default_admin = f"""
                INSERT INTO Admin
                    VALUES ( {admin_id.id}, "SterDevs", "{sterdevs_default_password}"),
                           ( {admin_id.id}, "Esprit", "{esprit_default_password}"),
                           ( {admin_id.id},"admin", "{admin_default_password}");
            """

            self.executeScript(create_default_admin)

    @staticmethod
    def adminConnected():
        conn = sqlite3.connect(_DATABASE_PATH_)
        cursor = conn.cursor()
        
        result = cursor.execute(f"""SELECT id, login, password
                                    FROM Admin
                                    WHERE status="connected" 
                                """)\
                        .fetchone()
        
        cursor.close()
        conn.close()
        
        return result
        
    @staticmethod
    def updateAdmin(id, new_login, new_password):
        
        conn = sqlite3.connect(_DATABASE_PATH_)
        cursor = conn.cursor()
        
        cursor.execute(f"""UPDATE Admin 
                            SET login="{new_login}", password="{new_password}"
                            WHERE  id={id};""")
        
        cursor.close()
        conn.commit()
        conn.close()

    @staticmethod
    def checkIfAdminExist(login, password):
        
        conn = sqlite3.connect(_DATABASE_PATH_)
        cursor = conn.cursor()
        
        result = cursor.execute(f"""
                            SELECT id, login, password FROM Admin
                            WHERE  login="{login}" AND password="{password}"
                        """).fetchone()
        
        cursor.close()
        conn.close()
        
        return result

    @staticmethod
    def connectAdmin(id):
        conn = sqlite3.connect(_DATABASE_PATH_)
        cursor = conn.cursor()
        
        cursor.executescript(f"""UPDATE Admin 
                                SET status="connected" 
                                WHERE id={id};
                            """)
        cursor.close()
        conn.commit()
        conn.close()
    
    @staticmethod
    def disconnectAdmin():
        conn = sqlite3.connect(_DATABASE_PATH_)
        cursor = conn.cursor()
        
        cursor.executescript(f"""UPDATE Admin 
                                SET status="disconnected";""")

        cursor.close()
        conn.commit()
        conn.close()
    

class StudentModel:

    name_separator = " _ "

    @staticmethod
    def getStudentPictures(register_number: str) -> list:
        assert isinstance(register_number, str)

        query = f"""
            SELECT path 
            FROM Picture, Student
            WHERE student_id=Student.id 
                    AND register_number="{register_number}";
        """

        result = DB.executeQuery_(query)

        if not result:
            return []

        pictures_paths = [ path for path, in result ]

        return pictures_paths

    @staticmethod
    def getStudentFaceEncodings(register_number: str) -> list:
        assert isinstance(register_number, str)

        query = f"""
            SELECT face_encoding 
            FROM Picture, Student
            WHERE student_id=Student.id 
                    AND register_number="{register_number}";
        """

        result = DB.executeQuery_(query)

        if not result:
            return []

        face_encodings = [ json.loads(face_encoding) for face_encoding, in result ]

        return face_encodings

    @staticmethod
    def addStudentPicture(picture_path: str, register_number:str):
        
        assert isinstance(picture_path, str)
        assert isinstance(register_number, str)


        student = StudentModel.findStudent(register_number)

        if not student:
            raise ValueError("The register number doesn't match any student!")

        try:
            
            q = f"SELECT * FROM Picture WHERE path='{picture_path}';"
            result = DB.executeQuery_(q)
            
            if not result:
            
                if not os.path.exists(picture_path):
                    raise ValueError("The picture file doesn't exist!")
                elif not picture_path.endswith((".png", ".jpg", ".jpeg")):
                    raise ValueError("A picture is required, either png, jpg or jpeg")
                
                #Get face encoding
                picture = fr.load_image_file(picture_path)

                face_encoding = fr.face_encodings(picture)[0]
                face_encoding_str = json.dumps(face_encoding, cls=NumpyArrayEncoder)

                picture_id = ID_Generator("Picture")

                query = f"""
                    INSERT INTO Picture(id, student_id, path, face_encoding)
                        VALUES ({picture_id.id}, {student["id"]}, "{picture_path}", "{face_encoding_str}");
                """

                DB.executeScript_(query)

        except:
            raise ValueError("The picture is not correct!")
        else:
            print("Face encoding successfully added !")

    @staticmethod
    def findStudent(register_number: str):
        assert isinstance(register_number, str)

        from ..model.Student import Student

        query = f"""
            SELECT Student.name, Student.surname, Student.level, Student.id,
                    Axe.name, Discipline.name 
            FROM Student, Axe, Discipline
            WHERE register_number="{register_number}"
                  AND Student.axe_id=Axe.id 
                  AND Axe.discipline_id=Discipline.id;
        """

        result = DB.executeQuery_(query)

        if not result:
            return None

        student = result[0]
        
        name = student[0] + StudentModel.name_separator + student[1]
        level = student[2]
        id = student[3]
        axe = student[4]
        discipline = student[5]
        
        student = Student(name, register_number, level)
        student["id"] = id
        student["axe"] = axe
        student["discipline"] = discipline

        return student

    @staticmethod
    def removeStudent(register_number: str):
        
        query = f"""
            DELETE FROM Picture
                WHERE student_id IN (SELECT id FROM Student 
                                        WHERE register_number="{register_number}");
        """

        DB.executeScript_(query)
        
        query = f"""
            DELETE FROM Student
                WHERE register_number="{register_number}";
        """

        DB.executeScript_(query)
        
    @staticmethod
    def insertStudent(student: dict, axe: str) -> None:
        print("[Static] insertStudent")

        student_id_gen = ID_Generator("Student")
        student_id = student_id_gen.id

        axe_id = AxeModel.getID(axe)

        name, surname = student["name"].split(StudentModel.name_separator)
        register_number = student["register_number"]
        level = student["level"]
        
        if StudentModel.findStudent(register_number):
            raise ValueError("Student already exist")

        query = f"""
            INSERT INTO Student(id, axe_id, name, surname, register_number, level)
                VALUES ({student_id}, {axe_id}, "{name}", "{surname}", "{register_number}", {level});
        """

        DB.executeScript_(query)

    @staticmethod
    def updateStudent(student, axe) -> None:
        print("[Static] updateStudent")

        from ..model.Student import Student
        assert isinstance(student, Student)

        student_id = student.get('id')

        axe_id = AxeModel.getID(axe)

        name, surname = student["name"].split(StudentModel.name_separator)
        register_number = student["register_number"]
        level = student["level"]

        #Verify if other student have the same register number
        query = f"""
            SELECT id FROM Student
            WHERE register_number="{register_number}" 
                    AND id != {student_id}
        """

        if len(DB.executeQuery_(query)) > 0:
            raise ValueError("Two Students can't have the same register number !")
        

        query = f"""
            UPDATE Student
                SET axe_id={axe_id}, name="{name}", surname="{surname}", 
                    register_number="{register_number}", 
                    level={level} 
                WHERE id={student_id};            
        """

        DB.executeScript_(query)
        
        #
        # Update pictures
        #
        
        # for picture_path in student.get("pictures"):
        #     q = f"SELECT * FROM Picture WHERE path='{picture_path}';"
        #     result = DB.executeQuery_(q)
            
        #     if not result:
        #         try:
        #             StudentModel.addStudentPicture(picture_path, 
        #                                         student.get('register_number'))
        #         except ValueError:
        #             print(f"Error while trying to insert {picture_path}")
                
            

    @staticmethod
    def removePicture(path):
        assert isinstance(path, str)
        
        print("[RemovePicture] : ", path)

        query = f"""
            DELETE FROM Picture 
            WHERE path="{path}"
        """

        DB.executeScript_(query)

    @staticmethod
    def getStudents(axe: str, level: int) -> list:

        from ..model.Student import Student

        print("[Static] getStudents")

        assert isinstance(axe, str)
        assert isinstance(level, int)

        students = []

        query = f"""
                SELECT Student.name, Student.surname, Student.register_number
                FROM Student, axe
                WHERE axe_id=axe.id AND axe.name="{axe}" AND level={level}
        """

        data = DB.executeQuery_(query)

        if not data:
            return []

        for student in data:
            name = student[0] + StudentModel.name_separator + student[1]
            register_number = student[2]
            students.append( Student(name, register_number, level) )

        return students


class DisciplineModel:

    @staticmethod
    def getAxes(discipline_name):
        
        query = f"""SELECT Axe.name 
                    FROM Axe, Discipline
                    WHERE Axe.discipline_id=Discipline.id 
                            AND Discipline.name="{discipline_name}" 
        """

        response = [ axe for axe, in DB.executeQuery_(query) ]

        return response

    @staticmethod
    def getDisciplinesName():
        
        query = f"""SELECT name 
                    FROM Discipline;
        """

        response = [ discipline for discipline, in DB.executeQuery_(query) ]

        return response


class AxeModel:

    @staticmethod
    def getID(axe: str) -> int:
        assert isinstance(axe, str)

        query = f"""
            SELECT id FROM Axe WHERE name="{axe}"
        """ 

        axe_id = DB.executeQuery_(query=query)

        if axe_id:
            axe_id, = axe_id[0]
            return axe_id
        else:
            raise ValueError("Undefined Axe ID !")
