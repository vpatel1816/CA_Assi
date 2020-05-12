a = str(input("enter the string"))
b=[]
for i in a.split():
   c= i[::-1]
   b.append(c)
x=" ".join(b)
print(x)
