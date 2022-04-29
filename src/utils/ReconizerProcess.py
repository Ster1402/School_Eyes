from time import ctime, sleep
from .FaceReconizer import FaceReconizer
from .VideoProvider import VideoProvider
from .Request import Request
import cv2
import asyncio
class TimerTest:

    def __init__(self) -> None:
        self.latency = 0.5

        self.i_test = 0
        self.j_test = 0

    def ShouldEndThread(self):
        self.i_test += 1
        return self.i_test == 10
        
    def ShouldProcessFrame(self):
        return True


class ReconizerProcess:

    def __init__(self, request: Request):
        assert isinstance(request, Request)

        #Request to process
        self.__request = request
        #Video provider
        self.__video_provider: VideoProvider = VideoProvider(self.__request["classroom"])
        #Timer to control the execution process
        self.__timer = TimerTest() #For test
        #Face reconizer
        self.__face_reconizer = FaceReconizer(self.__request["disciplines"], 
                                              self.__request["level"])
        #ListFormatter : To format the result
        self.__list_formatter = None

    async def RecognitionProcess(self) -> list:
        
        result = []        

        for frame in self.__video_provider.ProvideFrame():
            if not self.__timer.ShouldEndThread():
                                
                if self.__timer.ShouldProcessFrame():
<<<<<<< HEAD
                    print("Frame processed...")
                    rgb_frame = frame[:, :, ::-1]
                    students_detected = self.__face_reconizer.StudentsDetected(rgb_frame)
=======
                    
                    students_detected = await self.__face_reconizer.StudentsDetected(frame)
>>>>>>> d8308cedb69e5e6ef828932aa214276abd2ae8cb
                    time = ctime()
            
                    result.append({
                        "time": time,
                        "students": students_detected 
                    })
                
                else:
                    continue

                print('Sleep latency')                
                sleep(self.__timer.latency)

            else:

                break

        return result

