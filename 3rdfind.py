#!/usr/bin/python
import string

def test(a = 'book'):
    '''find characters from mess .

    '''
    fin = open(a)
    chars = ''
    for line in fin:
        words = line.strip()
        for ch in words:
            n = ord(ch)
            if n <= ord('z') and n >= ord('a'):
                chars += ch
            elif n <= ord('Z') and n >= ord('A'):
                chars += ch
    if len(chars) > 0:
        print chars
        #print chars

def __main__():
    print test.__doc__
    a = raw_input("Please input filename:");
    if bool(a) == False:
        test()
    else:
        test(a)

__main__()
