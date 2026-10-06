#!/usr/bin/env python3
import sys
text=[]
if len(sys.argv)<=1:
    print("none")
else:
    for x in sys.argv[1:]:
        text.append(x)

    i=len(text)-1
    while i>=0:
        print(text[i])
        i-=1
    