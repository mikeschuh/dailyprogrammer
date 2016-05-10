#

import sys


def sleep_sort(intlist):
	pass


def main():

	if len(sys.argv) == 1:
		print 'python 091e.py {list of ints to sort}'
		exit()

	intlist = sys.argv[1:]
	print intlist

	sleep_sort(intlist)


if __name__ == "__main__":
    main()
    
