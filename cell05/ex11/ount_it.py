#!/usr/bin/env python3
import sys
num=len(sys.argv)-1
text=sys.argv[1:]
i=0
if num <= 0:
    print("none")
else:
    print("parameters",num)
    while i < num:
        print(text[i],":",len(text[i]))
        i+=1