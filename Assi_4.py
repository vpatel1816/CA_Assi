#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:36:19 2020

@author: vish
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:47:01 2020
@author: vish
"""
"""
1
str=input("enter string") 
revstr=str[::-1] 
print(revstr)
"""
"""
2
j=(input("enter string")) 
print(j)
c=len(j)
u=0
l=0
for i in range(c): 
    if j[i].isupper():
        u+=1
    elif j[i].islower():
        l+=1
    elif j[i].isspace():
        pass
print("No. of Upper case characters", u ,"\nNo. of Lower case Characters : ", l)
"""
"""
3
def unielelist(inp): 
    y = []
    for i in inp:
        if i not in y:
            y.append(i)
    print(y, "uniques numbers are", len(y))
inp = input("enter the numbers") 
unielelist(inp)
"""
"""
4
inp=input("enter a string with - :")
c=[]
temp=""
for i in inp:
    if i =="-":
        pass
        c.append(temp)
        temp=""
    else:
        temp+=i
c.append(temp)
new=sorted(c)
print('-'.join(new))
"""
"""
5
paragph = []
while True:
    newline = input()
    if newline:
        paragph.append(newline.upper())
    else:
        break;
sortedpara=sorted(paragph)
for newline in sortedpara:
    print(newline)
"""
"""
6
def sum(dig1,dig2): 
    print(type(dig1)) 
    print(type(dig2)) 
    x=int(dig1) 
    y=int(dig2)
    sum = x+y
    print("sum of",x,"and",y,"is",sum) 
dig1=input("enter the firsr digit") 
dig2=input("enter the second digit") 
sum(dig1,dig2)
"""
"""
7
def bigstring(str1,str2):
    a = len(str1) 
    b = len(str2) 
    if a>b:
        print("String 1:", str1 ," is bigger than String 2: ",str2) 
    elif a<b:
        print ("String 2:", str2 ," is bigger than String 1: ", str1) 
    elif a==b:
        print ("string 1 and 2 has the same length")
str1 = input("please insert the first string") 
str2 = input("please insert the second string") 
bigstring(str1,str2)
"""
"""
8
def mynewfun(digit): 
    j = 1 + int(digit) 
    list = []
    for i in range(j):
        list.append(i**2)
        i+=1 
    print(list)
digit= input("please insert the limit value")
mynewfun(digit)
"""
"""
9
def showNumbers(limit): 
    j = 1 + int(limit)
    for i in range(0,j):
        if i%2==0:
            print(i, " is even")
        else:
            print(i, " is odd")
limit= input("please insert the limit value") 
showNumbers(limit)

"""
