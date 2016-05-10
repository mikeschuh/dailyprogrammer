#
import sys
import multiprocessing
import time

def sleep_sort_worker(num):
	time.sleep(num)
	print num


def sleep_sort(intlist):
	for num in intlist:
		p = multiprocessing.Process(target=sleep_sort_worker, args=(num,))
		p.start()


def main():

	if len(sys.argv) == 1:
		print 'python 091e.py {list of ints to sort}'
		exit()

	intlist = [int(x) for x in sys.argv[1:]]
	print intlist

	sleep_sort(intlist)


if __name__ == "__main__":
    main()
    
