from multiprocessing import RLock
import threading
import os
import json
import time

_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class RequestHandler(threading.Thread):
    __CONFIG_PATH = os.path.join(_ROOT_PATH, "config/")
    __CONFIG_FILE = os.path.join(__CONFIG_PATH, "config.json") 

    #To make each reconize process lock each other we needed
    semaphore = RLock()

    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "RequestHandler_Thread"

        self.clients = []
        self.requests = []
        self.host, self.port = self.__getServerInformation()

    def _writeDefaultConfig(self):
        default_host = ""
        default_port = 65_000

        data = {
            "Server": {
                "Host": default_host,
                "Port": default_port,
            },
        }

        #We write the default value in the file
        json.dump(data, open(self.__CONFIG_FILE, "w"), indent=4)
        
    def __getServerInformation(self):        
        default_host = ""
        default_port = 65_000
        data = {}

        if os.path.exists(self.__CONFIG_FILE) \
            and self.__CONFIG_FILE.endswith(".json"):

            with open(self.__CONFIG_FILE, 'r') as f:
                
                try:    
                    data = json.load(f)

                except json.decoder.JSONDecodeError:
                    print("[Error]: Empty data in:", self.__CONFIG_FILE)
                    self._writeDefaultConfig()
                    
                else:
                        if "Server" not in data:
                            data["Server"] = {
                                "Host": default_host,
                                "Port": default_port
                            }

                            json.dump(data, 
                                      open(self.__CONFIG_FILE, "w"), 
                                      indent=4)


            return (data.get("Server").get("Host"),
                    data.get("Server").get("Port"))

        else:
            #Create config.json
            
            os.makedirs(self.__CONFIG_PATH) 
            with open(self.__CONFIG_FILE, "w"):
                self._writeDefaultConfig()

            return (default_host, default_port)

    def run(self):
        print(self.name)
        self.ListenRequest()
        
        
    def DecodeRequest(self, request):
        #Decode here
        
        #....

        self.requests.append(request)

        return request

    def ListenRequest(self):
        print("Listening for request...")

        