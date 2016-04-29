#



class Rect:
    
    #rectangle from top-left to bottom-right
    def __init__(self,x1,y1,x2,y2):
        self.ulpt = (x1,y1)
        self.lrpt = (x2,y2)
        
    def disp(self):
        return "Rect(%i, %i, %i, %i)" % (self.ulpt[0], self.ulpt[1], self.lrpt[0], self.lrpt[1] )
    
    
def intersect_rectangles(a, b):
    
    ulxmax = max(a.ulpt[0], b.ulpt[0])
    ulymax = max(a.ulpt[1], b.ulpt[1])
    lrxmin = min(a.lrpt[0], b.lrpt[0])
    lrymin = min(a.lrpt[1], b.lrpt[1])
    
    xr = lrxmin - ulxmax
    yr = lrymin - ulymax
    if xr <= 0 or yr <= 0:
        return None
    
    res = Rect(ulxmax, ulymax, lrxmin, lrymin)
    return res

def main():
    
    r1 = Rect(3, 3, 10, 10)
    r2 = Rect(6, 6, 12, 12)
    
    print 'intersecting: ', r1.disp(), r2.disp()
    intrect = intersect_rectangles(r1, r2)
    
    if intrect == None:
        print 'No intersection'
    else:
        print 'Result: ', intrect.disp()

    #########
    r1 = Rect(4, 4, 5, 5)
    r2 = Rect(6, 6, 10, 10)
    
    print 'intersecting: ', r1.disp(), r2.disp()
    intrect = intersect_rectangles(r1, r2)
    
    if intrect == None:
        print 'No intersection'
    else:
        print 'Result: ', intrect.disp()



if __name__ == "__main__":
    main()
