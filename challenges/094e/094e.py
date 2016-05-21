#
import sys

element_lookup = ["Ac","Ag","Al","Am","Ar","As","At","Au","B","Ba","Be","Bh","Bi",
       "Bk","Br","C","Ca","Cd","Ce","Cf","Cl","Cm","Cn","Co","Cr","Cs",
       "Cu","Db","Ds","Dy","Er","Es","Eu","F","Fe","Fl","Fm","Fr","Ga",
       "Gd","Ge","H","He","Hf","Hg","Ho","Hs","I","In","Ir","K","Kr","La",
       "Li","Lr","Lu","Lv","Md","Mg","Mn","Mo","Mt","N","Na","Nb","Nd","Ne",
       "Ni","No","Np","O","Os","P","Pa","Pb","Pd","Pm","Po","Pr","Pt","Pu",
       "Ra","Rb","Re","Rf","Rg","Rh","Rn","Ru","S","Sb","Sc","Se","Sg","Si","Sm",
       "Sn","Sr","Ta","Tb","Tc","Te","Th","Ti","Tl","Tm","U","Uuo","Uup","Uus","Uut",
       "V","W","Xe","Y","Yb","Zn","Zr"]


def elementize(instr):
    # "breaking bad"-ify the string

    outstrs = []
    matchstr = instr.lower()

    for symbol in element_lookup:
        fi = matchstr.find(symbol.lower(), 0)
        while fi != -1:
            print fi
            l = len(symbol)
            tmpstr = instr[:fi] + '[' + symbol + ']' + instr[fi+l:]
            outstrs.append(tmpstr)
            fi = matchstr.find(symbol.lower(), fi+l)
    
    return outstrs


def main():

    instr = sys.argv[1]  # input string
    outstrs = elementize(instr)

    for outstr in outstrs:
        print outstr


if __name__ == "__main__":
    main()
