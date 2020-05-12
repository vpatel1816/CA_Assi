#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:06:57 2020

@author: vish
"""
  
""" lets keep it better not to keep it
las try to update

"""

"""

1

nub = int(input('enter a number: ')) 
if nub%3==0 and nub%5==0:
    print('Consultadd Python Training') 
elif nub%5==0:
    print('c')
elif nub%3==0:
    print('Consultadd')
else:
    print('not divisible by 3 or 5')


"""""""
2

print('Enter 1 - Addition\n', 'Enter 2 - Subtraction\n', 'Enter 3 - Division\n', 'Enter 4 - Multiplication\n', 'Enter 5 - Average\n')

nub = int(input('choose from the above option'))
if nub <=4:
    a = int(input('enter a number: '))
    b = int(input('enter a another number: '))
    if nub==1:
        var = a+b
        print (var)

    elif nub == 2:
        
        var = a - b
        print (var)
        c = str(var)
        if c.startswith('-'):
            print("NEGATIVE")
            
        

    elif nub == 3:
        
        var = a / b
        print (var)
    elif nub == 4:
        
        var = a * b
        print (var)
        
elif nub == 5:
    a = input('enter numbers seperated by spaces: ')
    b = a.split(' ')
    
    for i in range(0, len(b)):
        b[i] = int(b[i])
    
    Sum = sum(b) 
    average= Sum/len(b)  
    print (average)
    c = str(average)
    if c.startswith('-'):
        print("NEGATIVE")
        
"""
"""


3


a=int(input("enter number as a ")) 
b=int(input("enter number as b ")) 
c=int(input("enter number as c "))
sum=a+b+c
avg=sum/3
print("SUM is:",sum,", AVG is:",avg) 
if avg>a and avg >b and avg>c:
    print("Avg is higher than A B and C") 
else:
    if avg>a and avg>b:
        print("avg is higher than A and B")
    elif avg>b and avg>c:
        print("avg is higher than B and C")
    elif avg>a and avg>c:
        print("avg is higher than A and C")
    else:
        if avg>a:
            print("Avg is higher than A") 
        elif avg>b:
            print("Avg is higher than B") 
        elif avg>c:
            print("Avg is higher than C")

"""""""


4


while True:
    nub = int(input('enter a number: ')) 
    if nub>=0:
        print('Good Going')
        continue 
    if nub < 0:
        print("it's over") 
        break

"""""""

5


for i in range(2000, 3200): 
    if i%7==0 and i%5!=0:
        print(i)
        
        
"""
"""

6

Op 1 >
you can have for loop from i to integer value, can use range for that, like range(0,123) to have i from 0 to 123



op 2>
0 
1
2


op 3>
0
1 
2 
3 
4

"""""""


7

a = []
for i in range(0, 6):
    if i!=3 and i!=6: 
        a.append(i) 
        continue
print(a)


"""
"""


8

nub = input('enter a data to determine number of string or digit: ') 
letters = 0
digit = 0
for i in nub:
    if i.isalpha(): 
        letters+=1
    else: 
        digit+=1
print('you entered: ', nub, '\nLetters: ', letters, '\nDigits', digit) 

"""
"""


9

number = int(input('guess the lucky number ')) 
while number != 9:
    print('that is not lucky number ')
    answer = input('do you want to guess again? YES or NO ') 
    if answer=='yes':
        number = int(input('guess the lucky number '))
        continue
    elif number==9 or answer=="no":
        break
        
"""
"""


10

c=0
while c<5:
    xy=int(input("enter the number")) 
    c+=1
    if xy==10:
        print("Guessed correct")
    else:
        print("Try Again")
else:
    print("Game Over")


"""""""


11

c=0
a=[]
while c<5:
    xy=int(input("enter the number")) 
    c+=1
    if xy==10:
        print("Good guess!")
        a.append(xy) 
    else:
        print("Try Again") 
c=len(a)
for i in a:
    print("You guess it correct for",c,"times") 
    break
else:
    print("that was unsuccesfull")



"""




