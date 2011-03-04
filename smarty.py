#!/usr/bin/python

import urllib
import re
from PIL import Image as image

pic = "oxygen.png"
co = []
cur = ""
im = image.open(pic)
#for i in range (87):
#    pixel = im.getpixel((i*7,43))
#    cur += chr(pixel[0])
#print cur
for y in range (43,52):
    ch = ""
    for x in range (87): #629 - 21 = 608 608/7 = 89
        pixel = im.getpixel((x*7,y))
        cur = pixel[0]
        ch += chr(pixel[0])
    print ch

result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
nextw = ""
print result
for ch in result:
    nextw += chr(ch)
print nextw
