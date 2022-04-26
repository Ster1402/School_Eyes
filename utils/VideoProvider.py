import json
import cv2
from itertools import cycle
from time import sleep
import os

__ROOT__PATH = os.path.dirname( os.path.dirname(__file__) )
chemin = os.path.join(__ROOT__PATH, "config/", "config.json")

__classroom = "_15BS2"


def getCameras(sources):
    for video_source in sources.values():
        print(video_source, type(video_source))
            
        yield cv2.VideoCapture(video_source)

with open(chemin,"r") as file_json:
    config_file = json.load(file_json)
    sources = config_file["VideoSources"][__classroom]

def ProvideFrame(sources):
    for video_source in cycle(sources.values()):
        print(video_source, type(video_source))
        camera = cv2.VideoCapture(video_source)
        if camera.isOpened():
            is_frame_ready, frame = camera.read()
            if is_frame_ready:
                sleep(1)
                # cv2.imwrite("Frame.png", frame)
                yield frame
                sleep(1)

        camera.release()


for frame in ProvideFrame(sources):
    cv2.imwrite("Frame.png", frame)