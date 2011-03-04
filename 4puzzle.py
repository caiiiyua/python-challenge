#!/usr/bin/env python

import string
import re

def test(a = 'puzzle4'):
    '''Find characters match the condition .

    find letter XXXxXXX'''
    fin = open(a).read()
    chars = "".join(re.findall('(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)',fin))
    print chars


def __main__():
    print test.__doc__
    a = raw_input("Please input filename:\n");
    if bool(a) == False:
        test()
    else:
        test(a)

__main__()
