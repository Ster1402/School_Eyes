from utils import ReconizerProcess
from utils.RequestHandler import RequestHandler
import sys


def main(args):

	request_handler = RequestHandler()

	#We start listening for request
	request_handler.start()

	request_handler.join()

#Main program
if __name__ == '__main__':
	main(sys.argv)

