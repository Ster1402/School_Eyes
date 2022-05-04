from ..database.db import StudentModel

class Student(dict):

    def __init__(self, name, register_number="", level=3):
        self["name"] = name
        self["register_number"] = register_number
        self["level"] = level

        if register_number:
            self["pictures"] = StudentModel.getStudentPictures(register_number)
            self["face_encodings"] = self._EncodeFace()

    def __key(self):
        return (self["register_number"])

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__key() == other.__key()
        else:
            return NotImplemented

    def copy(self):
        new_student = Student(self["name"], "", level=self["level"])
        new_student["register_number"] = self["register_number"]
        
        return new_student

    def _EncodeFace(self) -> list:
        return StudentModel.getStudentFaceEncodings(self["register_number"])

    @staticmethod
    def getStudents(axe, level):
        return StudentModel.getStudents(axe, level)

