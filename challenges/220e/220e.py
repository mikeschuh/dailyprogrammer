#
import sys


def foo(line):
    
    punclist = [',',';','-',"'",'.','!','?']
    words = line[:-1].split(' ')
    newline = ""
    #print words
    for word in words:
        tokens = []
        for c in word:
            if c not in punclist:
                tokens.append(c.lower())
        tokens = sorted(tokens)
        j = 0
        nword = ""
        for i in range(len(word)):
            if word[i] not in punclist:
                
                newc = tokens[j]
                if word[i].isupper():
                    newc = tokens[j].upper()
                nword = nword + newc
                
                j += 1
            else:
                nword = nword + word[i]
        
        if len(newline) == 0:
            newline = nword
        else:
            newline = newline + " " + nword
    
    return newline

def main():
    
    fname = sys.argv[1]
    fin = open(fname, 'r')
    line = fin.readline()
    
    print(line)
    newline = foo(line)
    print(newline)
    

if __name__ == "__main__":
    main()


