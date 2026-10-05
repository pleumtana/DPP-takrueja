#!/usr/bin/env python3
number=int(input("Number:"))
if number > 25 :
    print("Error")
else:
    i=number
    while i <= 25:
        print(number,"*",i,"=",number*i)
        i += 1