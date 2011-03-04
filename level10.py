#!/usr/bin/python

import urllib
import re
import math

a = [1, 11, 21, 1211, 111221]

def seq(n):
    if n == 1:
        b.append(a[0])
        return a[0]
    elif n < 1:
        return "Please Input a right number!"
    new = say(str(seq(n - 1)))
    print "the",n - 1,"number's length is",len(str(new))
    b.append(new)
    return new

def say(num):
    seqs = ""
    print "length is:",len(num)
    while len(num) > 0:
        tn = num[0]
        cn = 0
        while (cn < len(num) and num[cn] == tn):
            cn += 1
        seqs += str(cn) + str(tn)
        if cn == len(num):
            break
        else:
            num = num[cn:]
    return int(seqs)

print a
while True:
    b = []
    n = raw_input("Input a number:")
    if int(n) == 0:
        break
    print seq(int(n))
    print b
