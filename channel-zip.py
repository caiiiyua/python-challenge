#!/usr/bin/python

import urllib
import re
import zipfile as zf

urlbase = "http://www.pythonchallenge.com/pc/def/channel.zip"
chainnum = "90052"
comments = ""
file = zf.ZipFile("temp/new.zip","r")
while True:
    data = file.read(chainnum + ".txt")
    print data
    chainnum = ''.join(re.findall('(?:nothing\s)(?:is\s)([0-9]{1,})',data))
    if len(chainnum) <= 0:
        break
    comments += file.getinfo(chainnum + ".txt").comment
print comments
