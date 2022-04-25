from operator import index
import os
import json
from aiohttp import web #For web async server
import socketio #To create a server
from .Request import Request

global _ROOT_PATH
_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class RequestHandler:
    __CONFIG_PATH = os.path.join(_ROOT_PATH, "config/")
    __CONFIG_FILE = os.path.join(__CONFIG_PATH, "config.json") 

    #Async Socket IO Server
    sio = socketio.AsyncServer()
    
    #Create new Aiohttp web Server
    app = web.Application()
    #Bind Socket IO to our web base server
    sio.attach(app)

    def __init__(self):
        self.name = "RequestHandler_Server"

        self.clients = set()
        self.requests = list()
        
        self.host, self.port = self.__getServerInformation()

        #Register event handler
        self.sio.on('client-request', self.ListenRequest)
        self.sio.on('disconnect', self.disconnect)
        self.sio.on('connect', self.connect)
    
        self._httpRoutes()


    def run(self, args):
        
        host = self.host if len(args) < 3 else args[1]
        port = self.port if len(args) < 3 else args[2]
        
        #Run the app
        web.run_app(app=self.app,
                    host=host,
                    port=port)
        
    def _httpRoutes(self):
        self.app.router.add_get('/', handler=self.index)

    #Index page : If a browse make a request
    async def index(self, request):
        print(request)
        #Getting index.html file
        index_file = os.path.join( _ROOT_PATH, 
                                "pages/",
                                "index.html")

        with open(index_file) as data: 
            return web.Response(text=data.read(), content_type="text/html")

    def _writeDefaultConfig(self):
        default_host = "0.0.0.0"
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
            if not os.path.exists(self.__CONFIG_PATH):            
                os.makedirs(self.__CONFIG_PATH) 
            
            with open(self.__CONFIG_FILE, "w"):
                self._writeDefaultConfig()

            return (default_host, default_port)


    def DecodeRequest(self, request):
        decoded_request = None
                 
        if isinstance(request, str):
            decoded_request = json.loads(request)
        elif isinstance(request, dict):
            decoded_request = request

        self.requests.append(decoded_request)

        return decoded_request

    """
    Events : 
        - connect : new client
        - disconnect : client disconnect
        - client-request : request for attendance list
    """

    @sio.on('connect')
    def connect(self, socket_id, environ, auth):
        self.clients.add(socket_id)
        print("Connected : ", socket_id)

    @sio.on('disconnect')
    def disconnect(self, socket_id, environ, auth):
        if socket_id in self.clients:
            self.clients.remove(socket_id)
        print("Disconnected : ", socket_id)

    #We listen for message
    @sio.on('client-request')
    async def ListenRequest(self, socket_id, request):

        print("Numbers : " , len(self.clients) )

        data = self.DecodeRequest(request)
        
        print("New request from:", socket_id, " request : ", request)

        #Process request here
        #
        #End 

        response = {**data}
        response["Provider"] = "School-Eyes"
        
        print("Response: ",response)

        await self.sio.emit('server-response', json.dumps(response), room=socket_id)

