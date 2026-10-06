#!/usr/bin/env python3
import sys
text = sys.argv[1:]
if len(text) == 0:
    print("none")
else:
    for x in text:
        if not x.endswith("ism"):
            print(x + "ism")