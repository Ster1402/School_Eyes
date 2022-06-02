import json
import cv2
from itertools import cycle
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
        print("[VideoProvider.ProvideFrame]")
        for video_source in cycle(self.__video_sources):

            camera = cv2.VideoCapture(video_source)

            print(f"[Camera retrieved : {video_source}]")

            fps = 0

            if camera.isOpened():

                print("[Camera opened!]")
                
                fps = 0

                while fps < 2:
                    fps += 1
                    is_frame_ready, frame = camera.read()
                    if is_frame_ready:
                        print("[Frame ready]")
                        
                        try:
                            print("[Convert frame to RGB]")
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        except:
                            print("[Error while trying to convert frame to RGB]")

                        yield frame
            else:
                print("[[Error] : Couldn't open camera!]")        
                yield None

            camera.release()
            print("[Camera closed]!")
