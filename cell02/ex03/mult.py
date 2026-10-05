#!/bin/env python3
nam_1=int(input("Number_1:"))
num_2=int(input("Number_2:"))
t_num=nam_1*num_2
if t_num > 0:
    print(t_num,"The result is positive.")
elif t_num < 0:
    print(t_num,"The result is negative.")
else:
    print(t_num,"The result is positive and negative.")