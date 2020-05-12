#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:02:34 2020

@author: vish
"""
"""

1,2




b=[]
b.append(-1) 
b.append(10.5) 
b.append("string") 
b.append(10+10j) 
print(b)
for i in b:
    print(type(i)) 
print(type(b)) 
print(type(tuple(b))) 
print(type(set(b))) 
print(type((b)))

"""
"""


2


b=[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17]

c=b[0:2] 
print(c)

c=b[1:3] 
print(c)

c=b[1:16:3] 
print(c)

c=b[::-1] 
print(c)

c=b[::-2] 
print(c)


"""
"""


3


b=[1,2,3,5,6] 
c=1
for i in b:
    c=c*i 
    print(c)


"""
"""


4

b=[1,2,3,4,5,6,7,8,9,2,7,45] 
print(max(b))
print(min(b))

"""
"""


5

b=[1,2,3,4,5,6,7,8,9,34,56,55,43,44,66,65,54,43,45,65,77,66,54,325,26,56,245,62,45,62,57,547,2,7,45] 
c=[]
for i in b:
    if i%2==0: 
        c.append(i)
    else: 
        continue
print(c)


"""
"""



6

b=[]
for i in range(1,31):
    if i<6 or i >25: 
        b.append(i**2)
    else: 
        b.append(i)
print(b)


"""
"""




7

array = [[1,3,5,7,9,10],[2,4,6,8]] 
new=array[0]
neww=array[1]
new.pop()
for i in neww: new.append(i)
print(new)


"""
"""


8

a={1:10,2:20} 
b={3:30,4:40} 
c={} 
c.update(a) 
c.update(b) 
print(c)



"""""""


9

nn=dict()
for x in range(1,10):
    nn[x]=x*x
print(nn) 

"""
"""

10 


a=input("Enter: ")
print(a.split(',')," - ",tuple(a.split(","))

      













