#

input = [123, 286, 196196871]

def is_palindrome(num):
    return num == int(str(num)[::-1])
    
def make_palindrome(num):
    """Returns the palindrome of an input number and how many steps to get it."""
    
    steps = 0
    while not is_palindrome(num):
        steps += 1
        revnum = int(str(num)[::-1])
        num = num + revnum
        
    return num, steps


if __name__ == "__main__":
    
    for num in input:
        revnum, steps = make_palindrome(num)
        print(num, ' became ', revnum, ' in ', steps, ' steps.')
