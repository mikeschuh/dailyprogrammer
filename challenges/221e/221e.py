#

import sys
import random


def turn():
    
    val = 0
    if random.random() >= 0.5:
        val = 1
    return val


def check_space(textarr, pos, angle):
    
    #if angle is 0, check left/right; 1, check up/down
    r,c = pos
    

def add_snake(textarr, pos, forward, tok):
    pass


def make_snake(textstr):
    
    textarr = []
    pos = (0,0)
    maxlen = 0
    forward = 1  # 0,1,2,3 => N,E,S,W
    if random.random() >= 0.5:
        forward = 2
    
    toks = textstr.split(' ')
    for tok in toks:
        add_snake(textarr, pos, forward, tok)
        
        
    
    return textstr

def main():
    
    fname = sys.argv[1]
    fin = open(fname, 'r')
    line = fin.readline()
    fin.close()
    
    snakelines = make_snake(line)
    
    fext = fname.split('.')[-1]
    fnameout = fname[:-1 * (len(fext)+1)] + "_out." + fext
    fout = open(fnameout, 'w')
    fout.writelines(snakelines)
    fout.close()
    

if __name__ == "__main__":
    main()
