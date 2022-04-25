
class Request(dict):

    def __init__(self, id, teacher, classroom, course, 
                disciplines, level, connection, launched_hour, finish_hour):

        self._verifyParam(id, teacher, classroom, course, 
                disciplines, level, connection, launched_hour, finish_hour)

        self["id"] = id
        self["teacher"] = teacher
        self["classroom"] = classroom
        self["course"] = course
        self["disciplines"] = disciplines
        self["level"] = level
        self["connection"] = connection
        self["launched_hour"] = launched_hour
        self["finish_hour"] = finish_hour

    def _verifyParam(self, id, teacher, classroom, course, 
                disciplines, level, connection, launched_hour, finish_hour):
                assert isinstance(teacher, str)
                assert isinstance(classroom, str)
                assert isinstance(course, str)
                assert isinstance(disciplines, list) or isinstance(disciplines, set)
                assert isinstance(level, int)
