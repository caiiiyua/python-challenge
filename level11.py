#!/usr/bin/python

import urllib
import re
from PIL import Image as image
from PIL import ImageDraw as draw
pic = "cave.jpg"
op = []
ep = []

im = image.open(pic)
pixel = list(im.getdata())
for y in range (im.size[1]):
    for x in range (im.size[0]):
        idx = y*640 + x
        if idx % 2 == 0:
            #im.putpixel((x,y),pixel[idx])
            ep.append(pixel[idx])
            im.putpixel((x,y),(0,0,0))
        else:
            op.append(pixel[idx])
            im.putpixel((x,y),(0,0,0))

even = image.new(im.mode, (im.size[0]/2,im.size[1]/2))
for y in range (even.size[1]):
    for x in range (even.size[0]):
        idx = y*640 + x
        if idx % 2 == 0:
            even.putpixel((x,y),op[idx])
even.save("even.jpg")

odd = image.new(im.mode, (im.size[0]/2,im.size[1]/2))
for y in range (odd.size[1]):
    for x in range (odd.size[0]):
        odd.putpixel((x,y),ep[idx])
odd.save("odd.jpg")

