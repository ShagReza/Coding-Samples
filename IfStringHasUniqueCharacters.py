# -*- coding: utf-8 -*-
"""
Sh Reza

CrackCoding 1.1- Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures
"""

# With using additional data structures
def Method1 (String):
    CharDict={}
    result = "All characters are unique!"
    for i, c in enumerate(String):
        if c in CharDict:
            result = "Repeated characters!"
            break
        CharDict[c]=i    
    return (result)


def Method2 (String):
    # there are 256 possible characters in an 8-bit extended ASCII character set (0 to 255)
    CharExistCheck= [False] * 256
    result = "All characters are unique!"
    for i, c in enumerate(String):
        if CharExistCheck[ord (c)]==True: # ord is for getting ascii code
            result = "Repeated characters!"
        else:
            CharExistCheck[ord (c)]=True
    return (result)


#Without using additional data structures
def Method3 (String):
    result = "All characters are unique!"
    for i in range (len(String)):
        for j in range (i):
            if i!=j:
                if String[i]==String[j]:
                    result = "Repeated characters!"
    return (result)

def Method4 (String):
    result = "All characters are unique!"
    SortedString=sorted(String)
    for i in range (len(String)-1):
        if SortedString[i]==SortedString[i+1]:
            result = "Repeated characters!"
    return (result)        



# Test:
String = "ABCDEF"
result=Method1(String)
print(result)
result=Method2(String)
print(result)
result=Method3(String)
print(result)
result=Method4(String)
print(result)

String = "ABCDEFA"
result=Method1(String)
print(result)
result=Method2(String)
print(result)
result=Method3(String)
print(result)
result=Method4(String)
print(result)

