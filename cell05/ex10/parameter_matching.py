#!/usr/bin/env python3
import sys
text_s=[]
num=len(sys.argv)-1
if num !=1:
    print("none")
else:
    text_s.append(sys.argv[1])
    text_in=input("Text:")
    if text_s[0]==text_in:
        print("Good job")
    else:
        print("Nope, sorry...")
