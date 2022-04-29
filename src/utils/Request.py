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
                socket_id : <id_du_socketio>,
                finish_hour : <heure_de_fin>
        }
"""

class Request(dict):

    def __init__(self, id=0, teacher="", classroom="", course="", 
                disciplines="", level=0, socket_id="", finish_hour=""):

        self._verifyParam(id, teacher, classroom, course, 
                         disciplines, level, socket_id, finish_hour)

        self["id"] = id
        self["teacher"] = teacher
        self["classroom"] = classroom
        self["course"] = course
        self["disciplines"] = disciplines
        self["level"] = level
        self["socket_id"] = socket_id
        self["finish_hour"] = finish_hour

    def _verifyParam(self, id, teacher, classroom, course, 
                disciplines, level, socket_id, finish_hour):
                assert isinstance(id, int)
                assert isinstance(socket_id, str)
                assert isinstance(teacher, str)
                assert isinstance(classroom, str)
                assert isinstance(course, str)
                assert isinstance(disciplines, list) or isinstance(disciplines, set)
                assert isinstance(level, int)

