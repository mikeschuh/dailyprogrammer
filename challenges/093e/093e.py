#
import sys

morsecode_lookup = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
                    'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
                    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
                    'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
                    'y':'-.--', 'z':'--..', ' ':' '}


def morse_encode(instr):

    outstr = ""
    for let in instr:
        tok = morsecode_lookup[let]
        outstr = outstr + tok + ' '
    outstr = outstr[:-1]
    return outstr


def morse_decode(instr):

    outstr = ""
    mkeys = morsecode_lookup.keys()

    tokens = instr.split(' ')
    for tok in tokens:
        # hack to catch consecutive spaces, which are parsed as empty
        # token strings and represent a true space in the string
        if len(tok) == 0:
            outstr = outstr + ' '
        else:
            for key in mkeys:
                if tok == morsecode_lookup[key]:
                    outstr = outstr + key

    return outstr


def main():
    
    encodestr = 'sos'
    decodestr = '... --- ...'
    # encodestr = 'hello world'
    # decodestr = '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'

    code = morse_encode(encodestr)
    print "'%s'  =>  '%s'" % (encodestr, code)
    text = morse_decode(decodestr)
    print "'%s'  =>  '%s'" % (decodestr, text)
    

if __name__ == "__main__":
    main()
