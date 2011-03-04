#!/usr/bin/python
import string

def test(a = 'doc'):
    '''Map characters to another.

    K->M
    O->Q
    E->G
    ...'''
    fin = open(a)
    for line in fin:
        chars = ''
        words = line.strip()
        for ch in words:
            n = ord(ch)
            if n <=ord('z') and n >=ord('A'):
                if n + 2 > ord('z'):
                    ch = chr(ord('a'))
                else:
                    ch = chr(n + 2)
            chars = chars + ch
        print chars

def __main__():
    print test.__doc__
    a = raw_input("Please input filename:");
    if bool(a) == False:
        test()
    else:
        test(a)

__main__()
