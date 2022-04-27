from pprint import pprint
from src.model.Axe import Axe
from ..database.db import DisciplineModel

class Discipline(dict):

    def __init__(self, name, level) -> None:
        assert isinstance(name, str)
        assert isinstance(level, int)

        self["name"] = name
        self["level"] = level
        
        axes_names = DisciplineModel.getAxes(name)

        self["axes"] = [ Axe(axe,level) for axe in axes_names ]

        print("++++++++++++++++++++++++++++++")
        print("Discipline:")
        pprint(self)
        print("------------------------------")
