from time import ctime, sleep
from pprintpp import pprint

from .Sender import Sender
from .ListFormatter import ListFormatter
from .FaceReconizer import FaceReconizer
from .VideoProvider import VideoProvider
from .Request import Request


class TimerTest:

    def __init__(self) -> None:
        self.latency = 5

        self.i_test = 0
        self.j_test = 0

    def ShouldEndThread(self):
        self.i_test += 1
        return self.i_test == 10
        
    def ShouldProcessFrame(self):
        self.j_test += 1
        return self.j_test % 3 != 0


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
        self.__list_formatter = ListFormatter(request)

        #Sender : To send the result to the shared database
        self.__sender = Sender(request)


    def RecognitionProcess(self) -> list:
        
        result: list = []        
        students: set = {}

        start_time = ctime()

        for frame in self.__video_provider.ProvideFrame():

            if not self.__timer.ShouldEndThread():
                                        
                if self.__timer.ShouldProcessFrame():
                    
                    if type(frame) == type(None):
                        continue

                    students_detected: set = self.__face_reconizer.StudentsDetected(frame)

                    if students_detected:
                        temp = []
                        temp.extend(students_detected)
                        temp.extend(students) 
                        print(temp)
                        students = set(temp) #We add students
                
                else:

                    if students:
                        #When we are done looking for students for a period of time
                        time = ctime()
                        result.append({
                            "time": time,
                            "students": set(students)
                        })

                    students = {}

                    sleep(self.__timer.latency)
                    #Restart the timer eventually
            else:
                break
        
        end_time = ctime()

        attendance_list = self.__list_formatter.FormattedList(result)

        attendance_list["start_time"] = start_time
        attendance_list["end_time"] = end_time
        attendance_list["course"] = self.__request["course"]

        pprint(attendance_list)

        #Send data to the client
        self.__sender.SendData(attendance_list)


        

