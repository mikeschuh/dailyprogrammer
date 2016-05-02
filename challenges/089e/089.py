#
import sys
import math


def test(data):

    #mean
    mu = sum(data) / float(len(data))
    
    #variance
    var = 0
    for v in data:
    	var += (v - mu)**2
    var = var / float(len(data))

    #standard deviation
    stdev = math.sqrt(var)
    print mu, var, stdev
    

def main():
    
    fstr = sys.argv[1]
    fin = open(fstr, 'r')
    data = [float(x) for x in fin.readlines()]
    
    test(data)
    

if __name__ == "__main__":
    main()
