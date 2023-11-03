# -*- coding: utf-8 -*-
"""
Sh Reza

CrackCoding 1.3- Write a method to replace all spaces in a string with '%20'.
"""

# using python functions
def Method1 (str1):
    return str1.replace(" ", "%20")


# without python functions and true length given with a fixed length array
def Method2(str1, lenStr):
    NumSpace=0
    for i, c in enumerate (str1):
        if c==" ":
            NumSpace=NumSpace+1
    Array=[None] * (lenStr+NumSpace*3) # 3 foe number of %20
    j=0
    for i,c in enumerate (str1):       
        if c==" ":
            Array[j]="%"
            Array[j+1]="2"
            Array[j+2]="0"
            j=j+3
        else:
            Array[j]=c
            j=j+1
    return(''.join(Array))
            

# Test:
str1="AB C  "
result=Method1(str1)
print(result)
result=Method2(str1,3)
print(result)