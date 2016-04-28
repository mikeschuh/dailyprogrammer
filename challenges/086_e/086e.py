#
import sys

def rle_encode(instr):
    
    bitpairs = []
    
    curkey = instr[0]
    curcnt = 1
    for c in instr[1:]:
        #print c
        if c == curkey:
            curcnt += 1
        else:
            bitpairs.append((curkey,curcnt))
            curkey = c
            curcnt = 1
    
    bitpairs.append((curkey,curcnt)) #don't forget last one
    
    return bitpairs
    
    
def rle_decode(incode):
    
    outstr = ""
    for bp in incode:
        outstr = outstr + bp[0]*bp[1]
    return outstr


def main():
    
    input_str = sys.argv[1]
    print 'input: ', input_str
    input_code = rle_encode(input_str)
    print 'rle encoding: ', input_code
    regen_str = rle_decode(input_code)
    print 'decoded: ', regen_str
    

if __name__ == "__main__":
    main()
