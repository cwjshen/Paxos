import sys
from helper import *
		
def main(argv):
	if (len(argv) != 2):
		print "Usage: python main.py <binary_string>"
	else:
		binary_x(argv[1], "")
	return

main(sys.argv)