#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 18:47:43 2020

@author: vish
"""

"""
1.	Write a program to Python find the values which is 
not divisible 3 but is should be a multiple of 7. 
Make sure to use only higher order function


Code:

limit=int(input("Enter the limit: "))
print([i for i in range(0,limit) if i%3!=0 and i%7==0])

Output:
    
Enter the limit: 100
[7, 14, 28, 35, 49, 56, 70, 77, 91, 98]



Enter the limit: 25
[7, 14]   


"""

"""
2. 	Write a program in Python to  multiple the element of list by itself using traditional
 function and pass the function to map to complete the operation.

l=[1,2,3,4]
n=[]
def new():
    for i in l:
        n.append(i*i)

"""
"""

3. 	Write a program to Python find out the character in a string which is 
uppercase using list comprehension.


inp=str(input("Enter the String"))
c = [i for i in inp if i.isupper()]
print(c)




"""
"""




4. 	Write a program to construct a dictionary from the two lists containing the names of
students and their corresponding subjects. The dictionary should maps the students with 
their respective subjects. Let’s see how to do this using for loops and dictionary 
comprehension. HINT-Use Zip function also
Student = ['Smit', 'Jaya', 'Rayyan']	
capital = ['CSE', 'Networking', 'Operating System']



# USING DICTIONARY COMPRE.

st = ['Smit', 'Jaya', 'Rayyan']	
ca = ['CSE', 'Networking', 'Operating System']
newd={st[i]:ca[i] for i in range(0, len(st))}
print(newd)


#USING ZIP FUNCTION 

st = ['Smit', 'Jaya', 'Rayyan']	
ca = ['CSE', 'Networking', 'Operating System']
newdic=zip(st,ca)
print(dict(newdic))

"""

"""


5

Yield

Yield is used to transform a function to a generator.
with return in method it stops the execution, but generator with yield can resume the execution from where it left.
it works same like return, stops the execution and sends the value back to caller
 
Generator

Generators are basically a way to create iterators, its a function which returns the value(Yield)
and iterate it over and over

next()
Next is an inbuild method which gets the next item frm iterator by calling method __next__.


"""
"""



6. 	Write a program in Python using 
generators to reverse the string. 
Input String = “Consultadd Training”



def fun(str):
    yield str[::-1]
inp=str(input("Please enter a string: "))
var=fun(inp)
print(var.__next__())


#output
#runfile('/Users/vish/CA_Assi/Assi_6.py', wdir='/Users/vish/CA_Assi')

#Please enter a string: Consultadd Training
#gniniarT ddatlusnoC




"""
"""

7


decorator adds extra functionality to existing function without affecting it.




"""
"""

8

What is front end 

Front end is basically client side, whatever a user interacts with. a
nd back end is server side which can be interact by developers and organization members only.

Front end technology involves building the user interface like websites or web applications. 
which includes design of UI, structure, animation and flow of the website.

Front end Technologies
HTML , CSS, JavaScript, Angular, PHP - Facebook


"""

























