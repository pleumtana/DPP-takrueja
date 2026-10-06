#!/usr/bin/env python3
import sys
pa=[]
if len(sys.argv) < 3:
    print("none")
else:
    num_1 = int(sys.argv[1])
    num_2 = int(sys.argv[2])
    for x in range(num_1, num_2+1):
        pa.append(x)
    print(pa)