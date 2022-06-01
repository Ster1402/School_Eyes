
from pprintpp import pprint


class ListFormatter:

    def __init__(self, attendance_list) -> None:
        self.__attendance_list: dict = attendance_list
        print("[Unformatted List] : ")
        pprint(attendance_list)

    def FormattedList(self, data):
        
        #Response : attendance list
        res = {
            "level" : self.__attendance_list.get("level"),
            "classroom" : self.__attendance_list.get("classroom"),
            "teacher" : self.__attendance_list.get("teacher"),
            "concerned_disciplines" : self.__attendance_list.get("disciplines"),
            "disciplines" : dict()
        }

        entry_number = len(data)

        #We construct the attendance per discipline and axe
        for entry in data:
            #entry is a dict that has "time" and "students" keys
            for student in entry.get("students"):
                discipline_name = student["discipline_name"]
                axe_name = student["axe_name"]

                del student["discipline_name"]
                del student["axe_name"]

                if  discipline_name not in res["disciplines"]:
                    res["disciplines"][discipline_name] = dict()

                if axe_name not in res["disciplines"][discipline_name]:
                    res["disciplines"][discipline_name][axe_name] = set()
                
                if student not in res["disciplines"][discipline_name][axe_name]:
                    student["attendance_percentage"] = (1 / entry_number) * 100
                    res["disciplines"][discipline_name][axe_name].add(student)
                else:
                    ind = list(res["disciplines"][discipline_name][axe_name]).index(student)
                    new_student = list(res["disciplines"][discipline_name][axe_name])[ind]
                    res["disciplines"][discipline_name][axe_name].remove(new_student)

                    new_student["attendance_percentage"] += (1 / entry_number) * 100
                    res["disciplines"][discipline_name][axe_name].add(new_student)

        #Transform set to list to be JSON Serializable
        for discipline in res["disciplines"]:
            for axe, students in res["disciplines"][discipline].items():
                res["disciplines"][discipline][axe] = list(students)

        return res