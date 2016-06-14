#

input = [123, 286, 196196871]

def check_palindrome(num):
    
    numstr = str(num)
    strlen = len(numstr)
    half = int(len(numstr) / 2)
    for i in range(0,half):
        if numstr[i] != numstr[(-1*i)-1]:
            return False
    return True

def make_palindrome(num):
    """Returns the palindrome of an input number and how many steps to get it."""
    
    steps = 0
    done = check_palindrome(num)
    while not done:
        steps += 1
        revnum = int(str(num)[::-1])
        num = num + revnum
        done = check_palindrome(num)
    
    return num, steps


if __name__ == "__main__":
    
    for num in input:
        revnum, steps = make_palindrome(num)
        print(num, ' became ', revnum, ' in ', steps, ' steps.')
