#!/usr/bin/env python3
import sys
def downcase_it(s):
    return s.lower()
TEXT=sys.argv[1:]
if len(TEXT) == 0:
    print("none")
else:
    for i in TEXT:
        print(downcase_it(i))