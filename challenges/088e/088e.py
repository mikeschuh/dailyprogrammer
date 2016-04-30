#




def test2():
    
    ordmin = ord('A')
    ordmax = ord('Z')
    ordrange = ordmax - ordmin
    
    t1 = 'A'
    t2 = 'Z'
    t1i = ord(t1) - ordmin
    t2i = ord(t2) - ordmin
    
    print "%s + %s = %i + %i : " % (t1, t2, t1i, t2i)
    
    tdi = ((t1i + t2i) % 26) + ordmin
    td = chr(tdi)
    print tdi, td


def test():
    
    t1 = 'A'
    t2 = 'Z'
    t1i = ord(t1)
    t2i = ord(t2)
    
    print t1, t1i, chr(t1i)
    print t2, t2i, chr(t2i)
    


def vigenere_encode(textstr, keystr):
    
    klen = len(keystr)
    newkeystr = ""
    for i in range(len(textstr)):
        newkeystr += keystr[i%klen]
    
    print textstr
    print newkeystr
    
    cipher = ""
    for i in range(len(textstr)):
        cipher += chr((((ord(textstr[i]) - ord('A')) + (ord(newkeystr[i]) - ord('A'))) % 26) + ord('A') )
    
    print cipher
    return cipher

def main():

    test()
    test2()

    keystr = "GLADOS"
    plaintext = "THECAKEISALIE"
    pt2 = "HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLNBASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABBAISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISYMAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR"
    
    ciphertext = vigenere_encode(plaintext, keystr)
    
    
    

if __name__ == "__main__":
    main()
