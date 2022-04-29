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
                    
                    rgb_frame = frame[:, :, ::-1]
                    students_detected = await self.__face_reconizer.StudentsDetected(rgb_frame)
                    time = ctime()
                    
                    #cv2.imwrite('FrameVideo.png', frame)

                    result.append({
                        "time": time,
                        "students": students_detected 
                    })
                print('Sleep latency')                
                sleep(self.__timer.latency)

            else:

                break

        return result

