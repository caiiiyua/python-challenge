#!/usr/bin/env python

import string

realist = ""
le = []
def checkletter(le):
    for letter in le[:1]:
        if letter.isupper():
            return False
    for letter in le[1:4]:
        if letter.islower():
            return False
    for letter in le[4:5]:
        if letter.isupper():
            return False
    for letter in le[5:8]:
        if letter.islower():
            return False
    for letter in le[8:]:
        if letter.isupper():
            return False
    global realist
    realist += le[4]
    return True

def test(a = 'puzzle3'):
    '''Find characters match the condition .

    find letter XXXxXXX'''
    fin = open(a).read()
    chars = ''
#    for line in fin:
#        word = line.strip()
    for ch in fin:
        if ch != '\n':
            le.append(ch)
        if len(le) == 9:
            if checkletter(le):
                print le
                chars = "".join(le)
                print chars
                le.pop(0)
            else:
                le.pop(0)
    print realist

def __main__():
    print test.__doc__
    a = raw_input("Please input filename:\n");
    if bool(a) == False:
        test()
    else:
        test(a)

__main__()
