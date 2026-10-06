#!/usr/bin/env python3
import sys
num=len(sys.argv)-1
text=sys.argv[1:]
x=0
if num !=1 :
    print("none")
else:
    x=text[0].count('z')
    if x==0:
        print("none")
    else:
        print(x)