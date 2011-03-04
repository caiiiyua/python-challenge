#!/usr/bin/python

import urllib
import re
import pickle

urlbase = "http://www.pythonchallenge.com/pc/def/banner.p"

text = urllib.urlopen(urlbase)
word = pickle.load(text)
for le in word: # elements in the list
    ch = ""
    for ee in le: # elements in the elmenet set
        ch += ee[0]*ee[1]
    print ch


