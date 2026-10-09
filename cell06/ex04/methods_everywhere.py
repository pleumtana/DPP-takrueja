#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    while len(text) < 8:
        text += "Z"
    print(text)

texts = sys.argv[1:]

if len(texts) == 0:
    print("none")
else:
    for text in texts:
        n = len(text)

        if n > 8:
            shrink(text)
        elif n < 8:
            enlarge(text)
        else:
            print(text)