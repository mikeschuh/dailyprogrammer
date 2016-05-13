#
import sys
import pdb

ssd_lookup = {'0':'1111110', '1':'0110000', '2':'1101101', 
              '3':'1111001', '4':'0110011', '5':'1011011',
              '6':'1011111', '7':'1110000', '8':'1111111', '9':'1111011'}
#ABCDEFG

#each number is 2*s + 3 characters tall and 1*s + 2 wide
#so scale factor 1 = 5x3; 2 = 7x4
#                             +--+  +--+
#    +-+   +A+                |  |  |  |               
#    | |   F B                |  |  |  |
#    +-+   +G+    (s=2 =>)    +--+  +--+
#    | |   E C                |  |  |  |
#    +-+   +D+                |  |  |  |
#                             +--+  +--+

def ssd_convert2(digit, scale):
    #ssd_code = ssd_lookup(digit)
    #walk thru each line based on code

    dlines = []
    hbar = "-"*scale
    hgap = " "*scale
    csym = " "

    code = ssd_lookup[digit]
    tmpline = ""

    #topbar
    tmpline = hgap
    if code[0] == '1':
        tmpline = hbar
    tmpline = csym + tmpline + csym
    dlines.append(tmpline)

    if code[5] == '1':
        tmpline = "|"
    else:
        tmpline = " "
    tmpline += hgap
    if code[1] == '1':
        tmpline += "|"
    else:
        tmpline += " "
    for i in range(scale):
        dlines.append(tmpline)

    #midbar
    tmpline = hgap
    if code[0] == '1':
        tmpline = hbar
    tmpline = csym + tmpline + csym
    dlines.append(tmpline)


    if code[4] == '1':
        tmpline = "|"
    else:
        tmpline = " "
    tmpline += hgap
    if code[2] == '1':
        tmpline += "|"
    else:
        tmpline += " "
    for i in range(scale):
        dlines.append(tmpline)

    #bot bar
    tmpline = hgap
    if code[0] == '1':
        tmpline = hbar
    tmpline = csym + tmpline + csym
    dlines.append(tmpline)

    return dlines







def ssd_convert(digit, scale):
    #ssd_code = ssd_lookup(digit)
    #walk thru each line based on code

    dlines = []
    hbar = "-"*scale
    hgap = " "*scale

    if digit == '0':
        dlines.append("+" + hbar + "+")
        for i in range(scale):
            dlines.append("|" + hgap + "|")
        dlines.append("+" + hgap + "+")
        for i in range(scale):
            dlines.append("|" + hgap + "|")
        dlines.append("+" + hbar + "+")

    elif digit == '1':
        dlines.append(" " + hgap + "+")
        for i in range(scale):
            dlines.append(" " + hgap + "|")
        dlines.append(" " + hgap + "+")
        for i in range(scale):
            dlines.append(" " + hgap + "|")
        dlines.append(" " + hgap + "+")
    
    #pdb.set_trace()
    return dlines






def ssd_print(numstr, scaling):
    strlines = []
    
    for i in range((scaling*2)+3):
        strlines.append('')
    gapstr = ' ' * scaling

    for digi in numstr:
        dlines = ssd_convert2(digi, scaling)
        for i in range(len(strlines)):
            strlines[i] += gapstr + dlines[i]

    print ''
    for line in strlines:
        print line
    print ''
    

   

def main():

    scaling = 2
    while True:
        numstr = raw_input("Enter a number (q to quit): ")
        if numstr == 'q':
            break
        ssd_print(numstr, scaling)

if __name__ == "__main__":
    main()
    
