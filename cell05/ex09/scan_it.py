#!/usr/bin/env python3
import sys
num=len(sys.argv)-1
text_1=[]
text_2=[]
so=0
if num<=1 or num>2:
    print("none")
else:
    text_1.append(sys.argv[1])
    text_2.append(sys.argv[2])
    if text_1[0] in text_2[0]:
        print(text_2[0].count(text_1[0]))