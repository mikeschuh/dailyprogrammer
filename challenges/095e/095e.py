#
import sys


def main():
    
    fname = sys.argv[1]
    fin = open(fname, 'r')
    lines = [ln.split(' ') for ln in fin.readlines()]
    print lines
    
    # reverse lines function
    rlines = []
    for i in range(len(lines)-1, -1, -1):
        print i
        ln = lines[i]
        rln = ""
        for j in range(len(ln)-2, -1, -1):
            rln = rln + ln[j] + ' '
        rln = rln + ln[-1] # last token is also return characters included
        rlines.append(rln)
    ####
    
    outname = fname[:-4] + "_reversed.txt"
    fout = open(outname, 'w')
    fout.writelines(rlines)

if __name__ == "__main__":
    main()
