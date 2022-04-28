from src.utils.RequestHandler import RequestHandler
import sys

def main(args):
	request_handler = RequestHandler()
	request_handler.run(args)

#Main program
if __name__ == '__main__':
	main(sys.argv)



