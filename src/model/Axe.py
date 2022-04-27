from pprint import pprint
from .Student import Student


class Axe(dict):

    def __init__(self, name, level) -> None:
        self["name"] = name
        self["level"] = level
        self["students"] = Student.getStudents(axe=name, level=level)

        print("++++++++++++++++++++++++++++++")
        print("Axe:")
        pprint(self)
        print("------------------------------")