from pprint import pprint
from src.utils.ReconizerProcess import ReconizerProcess
import sys
import asyncio

from src.utils.Request import Request

async def main(args):
	test = await ReconizerProcess(request=Request(classroom="test", 
									disciplines=[{"name":"GIT", "axes":["GLO"]}],
									level=3
									)
					).RecognitionProcess()
	pprint(test)
	# request_handler = RequestHandler()
	# request_handler.run(args)

#Main program
if __name__ == '__main__':
	asyncio.run(main(sys.argv), debug=True)


