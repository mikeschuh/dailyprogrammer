#
import sys

def main():
    
    if len(sys.argv) == 1:
        print("python 217e.py inputfile")
        exit()
    
    fin = open(sys.argv[1], 'r')
    lines = fin.readlines()
    m = int(lines[0])
    n = int(lines[1])
    piles = []
    for line in lines[2:]:
        tmp = []
        tokens = line.strip().split(' ')
        for token in tokens:
            if len(token) > 0:
                tmp.append(int(token))
        piles.append(tmp)
        
        #piles.append([int(x) for x in line.split(' ')])
        # brute forced above to account for multiple spaces between tokens 
    
    for row in piles:
        print(row)
    
    low = min([min(x) for x in piles])
    #print(low)
    
    while n > 0:
        i = 0
        j = 0
        while i < m and n > 0:
            while j < m and n > 0:
                #print(i,j)
                if piles[i][j] == low:
                    #print('add')
                    piles[i][j] += 1
                    n = n - 1
                j += 1
            j = 0
            i = i + 1            
        low += 1
    
    
    for row in piles:
        print(row)
        
    

if __name__ == "__main__":
    main()
    
