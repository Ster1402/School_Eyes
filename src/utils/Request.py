""" Request : <dict>
        {
                id : <id_enseignant>,
                teacher : <nom_enseignant>,
                classroom : <salle_de_cours>,
                course : <cours_en_question>,
                level : <niveau_etudiants>,
                disciplines : [
                        {
                                name : <nom_filiere>,
                                axes : [<nom_des_axes>, ...]
                        },
                        ...
                ],
                finish_hour : <heure_de_fin>
        }
"""

class Request(dict):

    def __init__(self, id=0, teacher="", classroom="", course="", 
                disciplines="", level=0, finish_hour=""):

        self._verifyParam(id, teacher, classroom, course, 
                         disciplines, level, finish_hour)

        self["id"] = id
        self["teacher"] = teacher
        self["classroom"] = classroom
        self["course"] = course
        self["disciplines"] = disciplines
        self["level"] = level
        self["finish_hour"] = finish_hour

    def _verifyParam(self, id, teacher, classroom, course, 
                disciplines, level, finish_hour):
                assert isinstance(id, int)
                assert isinstance(teacher, str)
                assert isinstance(classroom, str)
                assert isinstance(course, str)
                assert isinstance(disciplines, list) or isinstance(disciplines, set)
                assert isinstance(level, int)
                assert isinstance(finish_hour, str)
