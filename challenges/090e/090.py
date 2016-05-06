#
import sys


def display(imgrid):

	for line in imgrid:
		for tok in line:
			print tok,
		print ''


def prog(w, h, moves):

	imgrid = []
	for i in range(h):
		imgrid.append([0] * w)

	r = c = 0
	for m in moves:
		if m == 'N':
			r = max(0,r - 1)
		elif m == 'S':
			r = min(h, r + 1)
		elif m == 'W':
			c = max(0,c - 1)
		elif m == 'E':
			c = min(w,c + 1)
		elif m == 'P':
			imgrid[r][c] = 1



	display(imgrid)



def main():

	if len(sys.argv) == 1:
		print "python 090.py {input file}"
		exit()

	fin = open(sys.argv[1], 'r')
	line = fin.readline()
	fin.close()

	w, h, moves = line.split(' ')

	prog(int(w), int(h), moves)




if __name__ == "__main__":
    main()
    

