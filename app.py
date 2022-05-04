import sys
from src.utils.RequestHandler import RequestHandler

def  main(argv):
	request_handler = RequestHandler()
	request_handler.run(argv)

#Main program
if __name__ == '__main__':
	main(sys.argv)

