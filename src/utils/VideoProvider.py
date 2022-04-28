import json
import cv2
from itertools import cycle
from time import sleep
import os
class VideoProvider:

    __ROOT__PATH = os.path.dirname( os.path.dirname(__file__) ) #...src/
    __CONFIG_FILE = os.path.join(__ROOT__PATH, "config/", "config.json")

    def __init__(self, classroom: str):
        assert isinstance(classroom, str)

        self.__classroom: str = classroom
        self.__video_sources: set = self._getVideoSources()

    def _getVideoSources(self) -> set:
    
        if not os.path.exists(VideoProvider.__CONFIG_FILE):
            raise ValueError("Can't find config.json file !")

        try:
            with open(VideoProvider.__CONFIG_FILE,"r") as config_file:
                configs = json.load(config_file)
        
                return set(configs["VideoSources"][self.__classroom].values())
        except Exception as err:
            raise ValueError("An error occurs while trying to retrieve cameras IP : ", err)


    def ProvideFrame(self):
        
        for video_source in cycle(self.__video_sources):

            camera = cv2.VideoCapture(video_source)
            print("Camera ok...")
            if camera.isOpened():
                is_frame_ready, frame = camera.read()
                if is_frame_ready:
                    sleep(1)
                    yield frame
                    sleep(1)
                    
            camera.release()
