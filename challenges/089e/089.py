#
import sys
import math


def get_mean(data):
    
    return sum(data) / float(len(data))
    
def get_variance(data):
    
    mu = get_mean(data)
    
    var = 0
    for v in data:
    	var += (v - mu)**2
    var = var / float(len(data))

    return var
    
def get_stdev(data):
    
    return math.sqrt(get_variance(data))
    

def get_all(data):
    
    mu = get_mean(data)
    var = get_variance(data)
    stdev = get_stdev(data)
    return mu, var, stdev

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
    
    #test(data)
    
    mu, var, stdev = get_all(data)
    print 'mean = ', mu
    print 'var = ', var
    print 'stdev = ', stdev
    

    

if __name__ == "__main__":
    main()
