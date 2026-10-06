#!/usr/bin/env python3
x=0
while x <= 10:   
    print("Table de",x,":",end=" ")
    i=0
    while i <=10:
        print(i*x,end=" ")
        if i==10:
            print("")
        i+=1
    x+=1