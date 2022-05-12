import json
import os
import sys

global _CONFIG_FILE

_ROOT_PATH = os.path.dirname( os.path.dirname(__file__) ) 
_CONFIG_FILE = os.path.join(_ROOT_PATH, "config/", "config.json")

class Classroom(dict):
    
    def __init__(self, name):
        self["name"] = name
        self["cameras"] = list()
        
    def getCameras(self):

        with open(_CONFIG_FILE, "r") as f:
            data = json.load(f)        
            
            classroom = data.get("VideoSources").get(f"_{self['name']}")
            
            cameras = []
            
            for camera in classroom:
                
                cameras.append({
                    "name": camera,
                    "url": classroom[camera]
                })

        return cameras
        
    @staticmethod
    def getClassroomsList():
        
        classrooms = list()
        
        with open(_CONFIG_FILE, "r") as f:
            data = json.load(f)        
            
            for classroom_name in data.get("VideoSources"):
                classrooms.append( classroom_name[1:] ) #We remove the underscore
        
        return classrooms