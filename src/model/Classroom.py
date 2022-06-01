import json
import os
import re

global _CONFIG_FILE

_ROOT_PATH = os.path.dirname( os.path.dirname(__file__) ) 
_CONFIG_FILE = os.path.join(_ROOT_PATH, "config/", "config.json")

class Classroom(dict):
    
    def __init__(self, name):
        self["name"] = name
        self["cameras"] = list()
        
    def getCameras(self):

        cameras = []

        with open(_CONFIG_FILE, "r") as f:
            data = json.load(f)        
            
            classroom_cameras = data.get("VideoSources").get(f"_{self['name']}")
            
            if not classroom_cameras:
                return list()

            for camera in classroom_cameras:
                
                cameras.append({
                    "name": camera,
                    "url": classroom_cameras[camera]
                })

        return cameras
    
    def removeCamera(self, camera):
    
        with open(_CONFIG_FILE, "r") as f:
            data: dict = json.load(f)        
            
            classroom_cameras = data.get("VideoSources").get(f"_{self['name']}")
            del classroom_cameras[camera]
            
            data["VideoSources"].update({
                f"_{self['name']}" : classroom_cameras
            })
        
        with open(_CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)
            
    def addCamera(self, url):
    
        with open(_CONFIG_FILE, "r") as f:
            data: dict = json.load(f)        
            
            classroom_cameras: dict = data.get("VideoSources").get(f"_{self['name']}")
            
            #Camera name
            id = 0
            for key in classroom_cameras.keys():
                pattern = r'[0-9]+'

                match = re.search(pattern, key)
                
                if not match:
                    continue
                
                temp_id = int(match.group())
                
                if temp_id > id:
                    id = temp_id

            id += 1
            camera_name = f"camera_{id}"
            
            classroom_cameras[camera_name] = url
            
            data["VideoSources"].update({
                f"_{self['name']}" : classroom_cameras
            })
        
        with open(_CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)
    
        
        return camera_name
        
    @staticmethod
    def getClassroomsList():
        
        classrooms = list()
        
        with open(_CONFIG_FILE, "r") as f:
            data = json.load(f)        
            
            for classroom_name in data.get("VideoSources"):
                classrooms.append( classroom_name[1:] ) #We remove the underscore
        
        return classrooms