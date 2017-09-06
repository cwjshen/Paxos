import sys, getopt
from helper import *

def main(argv):
	if (len(argv) < 3 or len(argv) > 4):
		print "Usage: python main.py <file-name> <gift card amount> <OPTION: 'triple' | 'pair'> "
		print "Example: 'python main.py prices.txt 2500 triple'"
	elif ((len(argv) == 4) and (argv[3] != 'triple') and (argv[3] != 'pair')):
		print "Usage: python main.py <file-name> <gift card amount> <OPTION: 'triple' | 'pair'> "
		print "Example: 'python main.py prices.txt 2500 triple'"
	else:
		print argv
		# Read the text file
		f = open(argv[1])

		# Parse through text file and store items in list
		item_list = []

		for line in f:
			item, price = line.strip().split(', ')
			item_list.append((item,int(price)))

		# Close file
		f.close()		

		# Total gift card amount
		gift_card = int(argv[2])

		if (len(argv) == 3):			
			print find_pair(item_list, gift_card)
		else:
			if (argv[3] == "pair"):
				print find_pair(item_list, gift_card)
			elif (argv[3] == "triple"):
				print find_triple(item_list, gift_card)

	return

main(sys.argv)