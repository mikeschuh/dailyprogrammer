#
import sys



def main():
    
    d = int(sys.argv[1])
    
    c = 1
    avail = 1
    
    while d >= 20:
        if avail == 0:
            d = d - 12
            avail = 3
        else:
            avail = avail - 1
            d = d - 20
            c = c + 1
    
    print 'total players: ', c


if __name__ == "__main__":
    main()
    
