#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:07:25 2020

@author: vish
"""

"""

#1.	Write a program that calculates and prints the value according to the given formula:
#Q= Square root of [(2*C*D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.



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



#2.  Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
#Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.






"""
"""

#3.  Create a class to find the three elements that sum to zero from a set of n real numbers.
#Input array: [-25,-10,-7,-3,2,4,8,10]
#Output: [[-10,2,8],[-7,-3,10]]


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
"""


#5.	Create a Time class and initialize it with hours and minutes.
#Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#Make a method displayTime which should print the time.
#Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.



class time():
    def __init__(self,t1h,t1m,t2h,t2m):
        self.t1h=t1h
        self.t1m=t1m
        self.t2h=t2h
        self.t2m=t2m
    def displayTime(self):
        print("Time 1:",t1h,"Hours and",t1m,"Mins.\nTime 2:",t2h,"hours and",t2m,"Mins.")
    def addTime(self):
        global th
        th=t1h+t2h
        global tm
        tm=t1m+t2m
        if tm>=60:
            th+=1
            tm-=60
        print("\nTotal time is: ",th,"Hours and",tm,"Minutes")
    def displayMinutes(self):
        totalmin=th*60+tm
        print("Only the Minutes: ",totalmin)
t1h=int(input("Enter the hour for first time: "))
t1m=int(input("Enter the minute for first time: "))
t2h=int(input("Enter the hour for second time: "))
t2m=int(input("Enter the miunte for first time: "))

t1=time(t1h,t1m,t2h,t2m)

t1.addTime()   
t1.displayTime()  
t1.displayMinutes()


"""
"""




#6.    Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter.
#The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , 
#the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance
#methods:
#yearPasses() should increase the  instance variable by .
#amIOld() should perform the following conditional actions:
#If , print You are young..
#If  and , print You are a teenager..
#Otherwise, print You are old..	


class person():
    
    def __init__(self,i):
        self.i=i
    def yearpasses(self):
        cy=1+i
        print("Passing year is",cy)
    def amiold(self):
        if i<=4:
            print("\nYou are a Todler")
        if i>4 and i<=12:
            print("\nYou are a kid")
        if i>12 and i<=20:
            print("\nTeen Ager")
        if i>21 and i<=59:
            print("\nMiddle age")
        if i>60:
            print("\nold")
inp=int(input("Input the limit you would like to check the ages"))
c=0
age=[]

for i in range(0,inp):
    new=int(input())
    age.append(new)
    
for i in age:
    if i<0:
        print("Invalid Age here", i, "Set to 0")
    else:
        o=person(i)
        o.amiold()
        o.yearpasses()





















