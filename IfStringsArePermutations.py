# -*- coding: utf-8 -*-
"""
Sh Reza

CrackCoding 1.2- Given two strings, write a method to decide if one is a permutation of the
other.
"""

# If sorting is allowed
def Method1 (str1, str2):
    str1=sorted(str1)
    str2=sorted(str2)
    if str1==str2:
        result="They are permutation"
    else:
        result="They are different"
    return result
   

# If sorting is not allowed
def Method2 (str1, str2):
    dic1={}
    dic2={}
    for i, c in enumerate(str1):
        if c in dic1:
            dic1[c]+1
        else:
            dic1[c]=1
    for i, c in enumerate(str2):
        if c in dic2:
            dic2[c]+1
        else:
            dic2[c]=1
    if dic1==dic2:
        result="They are permutation"
    else:
        result="They are different"
    return result


# if white space are not important: "  AB" is considered permutation of "BA"
# solution: just removespace at first
# str1=str1.replace (" " , "")

# if it is not case sensetive
# solution: make all lower case
# str1=str1.lower()

# Test:
str1="ABC"
str2="BDC"
result=Method1(str1, str2)
print(result)
result=Method2(str1, str2)
print(result)

str1="ABC"
str2="BCA"
result=Method1(str1, str2)
print(result)
result=Method2(str1, str2)
print(result)