#
import sys


def run(mat):

    print mat
    rc = len(mat)
    cc = len(mat[0])

    # sum each row
    # sum each col
    rsums = [0] * rc
    csums = [0] * cc

    for ri in range(rc):
        for cj in range(cc):
            val = mat[ri][cj]
            print ri, cj, val
            rsums[ri] += val
            csums[cj] += val
    
    print 'row sums: ', rsums
    print 'col sums: ', csums
    
    # print rows sorted by row sum
    # print cols sorted by col sum
    rsums_sorted = sorted(rsums)
    print rsums_sorted
    ro = []
    rowmat = []
    for ri in range(rc):
        for rj in range(rc):
            if rsums[ri] == rsums_sorted[rj]:
                ro.append(rj)
                break

    print ro
    for ri in range(rc):
        rowmat.append(mat[ro[ri]])

    print 'row sorted:'
    print rowmat

    co = []
    colmat = []
    csums_sorted = sorted(csums)
    print csums_sorted
    for ci in range(cc):
        for cj in range(cc):
            if csums[ci] == csums_sorted[cj]:
                co.append(cj)
                break
    print co
    for rj in range(rc):
        tmp = [0] * cc
        for ci in range(cc):
            tmp[co[ci]] = mat[rj][ci]
        colmat.append(tmp)

    print 'col sorted:'
    print colmat
    
    
def readfile(fname):
    datamat = []
    with open(fname, 'r') as f:
        for line in f:
            # split on whitespace and cast as ints
            tokens = [int(x) for x in line.split(' ')]
            datamat.append(tokens)
    
    return datamat


def main():
    
    dfile = sys.argv[1]
    
    # read file
    data = readfile(dfile)

    # run matrix stuff
    run(data)


if __name__ == "__main__":
    main()
