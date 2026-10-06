#!/usr/bin/env python3
ar_1=[2, 8, 9, 48, 8, 22, -12, 2]
ar_2=[]
ar_3=[]

print("Original array:",ar_1)
for x in ar_1:
    if x >=5 :
        ar_2.append(x+2)
for x in ar_2:
    if x not in ar_3:
        ar_3.append(x)
    



print("New array:",ar_3)

