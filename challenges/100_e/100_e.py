
import sys


def run(mat):
    
    print mat
    
    rc = len(mat)
    cc = len(mat[0])
    
    #sum each row
    #sum each col
    rsums = [0] * rc
    csums = [0] * cc
    
    for ri in range(rc):
        for cj in range(cc):
            val = int(mat[ri][cj])
            print val
            rsums[ri] += val
            csums[cj] += val
    
    print 'row sums: ', rsums
    print 'col sums: ', csums        
    
    #print rows sorted by row sum
    #print cols sorted by col sum
    
    

def readfile(fname):
    datamat = []
    with open(fname, 'r') as f:
        for line in f:
            tokens = line.split(' ') #drop newline, then split on whitespace
            datamat.append(tokens)
    
    return datamat

def main():
    
    dfile = sys.argv[1]
    
    #read file
    data = readfile(dfile)

    #run matrix stuff
    run(data)


if __name__ == "__main__":
    main()
