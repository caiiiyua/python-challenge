#!/usr/bin/python

import urllib
import re

urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
chainnum = "12345"
for i in range (0,400):
    print  "open url " + urlbase + chainnum
    text = urllib.urlopen(urlbase + chainnum)
    word = text.read()
    print word
    chainnum = ''.join(re.findall('(?:nothing\s)(?:is\s)([0-9]{1,})',word))
    if len(chainnum) <= 0:
        chainnum = raw_input("Please input a new number:")

print urlbase + chainnum
#f.close()

