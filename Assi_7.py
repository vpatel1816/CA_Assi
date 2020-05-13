#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:07:25 2020

@author: vish
"""

"""
1
1.	Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.



import math

class calculationn():
    
    def __init__(self,D):
        self.D=D
        
    def formula(self):
        C=50
        H=30
        Q = (2*C*D)/H
        print(Q)
        Q=float(math.sqrt(Q))
        print("Squareroot of is: ", Q)
        
        
D=int(input("Enter the Value of D: "))
q1 = calculationn(D)
q1.formula()

"""
"""



2.  Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.



class shape():
    def area(self):
        print("In the class Shape where Area is default: 0")
class square():
    def __init__(self,length):
        self.length=length
        area=int(length)*2
        print("Init method of square where are is: ", area)
length=(input("Enter the Length: "))
o=shape()
o.area()
o1=square(length)


"""
"""

3.  Create a class to find the three elements that sum to zero from a set of n real numbers.
Input array: [-25,-10,-7,-3,2,4,8,10]
Output: [[-10,2,8],[-7,-3,10]]


class elementt():
    def __init__(self,li):
        self.li=li
    def logic(self):
        temp=[]
        out=[]
        for i in li:
            for j in li:
                for k in li:
                    if i+j+k==0:
                        temp.append(i)
                        temp.append(j)
                        temp.append(k)
                        out.append(temp)
                        temp=[]
        return out               
                        
limit=input("Enter the limit: ")
li=[] 
for i in range(0,int(limit)):
    c=int(input("Element: "))
    li.append(c)
o=elementt(li)
print(o.logic())


"""






















