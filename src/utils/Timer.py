from time import time
from datetime import datetime
import calendar

class Timer:
    
    # Test version
    def __init__(self):
        self.latency = 300
        self.finish_hour = "2022-05-10 22:05:00"
    
    # Test version    
    def convert_date_to_second():
        finish_hour = "2022-05-31 15:23:00"
        #Converts a string date "YYYY-MM-DD  HH:MM:SS" as a time in sec since EPOCH.
        #self.finish_date = datetime.strptime(self.finish_hour, '%Y-%m-%d %H:%M:%S')
       # self.finish_date = calendar.timegm(datetime.strptime(self.finish_hour, '%Y-%m-%d %H:%M:%S').timetuple())
        return calendar.timegm(datetime.strptime(finish_hour, '%Y-%m-%d %H:%M:%S').timetuple())
 
    # Test version
    def ShouldEndThread(self):
        self.start_time = time()
        self.finish_date = Timer.convert_date_to_second()
        duration_of_course = (self.finish_date  - self.start_time)
        return duration_of_course
        
    # Test version
    def ShouldProcessFrame(self):
        self.j_test += 1
        return self.duration_of_course


 



