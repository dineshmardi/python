print("hello")
for i in range(10):
    print(i)
#print in different line
print("this ios my practice class\nand this is good")
print("hello everyone","hope you guys are doing well")
print(23)
a=20
print("my name is:",a)

#variables 
name="dinesh"
age=23
price=23.66
print("my name is:",name,"and my age is:",age)

#type of variables

print(type(name))
print(type(age))
print(type(price))
print(type(False))
print(type('a'))
print(type(None))
#primary datatypes---
"""integer
string
float
boolean
None"""

#print sum of two number
a=int(input("enter a number="))
b=int(input("enter another number="))
print("the sum is=",a+b,"and the difference is=",a-b)

#arithematic operator

a=8
b=4
sum=a+b
print(a/b)
print(a%b)#remainder
print(a*b)
print(a-b)
print(a**b)
print(sum)

#relational operator
#its return only true or false

print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
a+=10;
print(a)
a,b

#logical operators

print(not False)#gives true


val1=True
val2=True
print(val1 and val2)

print((a==b)or(a>b))
a,b

#type conversion

# 1.type conversion ---automatic convertion

a=2
b=2.34
c=int("2")#casting or implicit change of datatypes 
sum=a+b
sum1=a+c
print(sum1)
print(sum)  #f;loat is superior
type(b)
# # 2.type casting -----type conversion manually

a=3.14
a=str(a)
type(a)#string typ

name=input("enter %d name="%a)
print(name)


number = 5  # For example
name = input(f"Enter a name {number}:")
print(name)
name


#write a program to input 2 number and print their sum
num1=int(input("enter anumber:"))
num2=int(input("enter anumber:"))
sum=num1+num2
print(f"sum of {num1} and {num2} is:",sum)

#writea program to input side of a square and print its area

side=float(input("enter the length of a square side:"))
area=side**2
print(f"area of square whose side is {side} is:{area} cm\u00B2")

#printing average of two number
num1=float(input("enter a number:"))
num2=float(input("enter a number:"))
avg=(num1+num2)/2
print(f"average of {num1} and {num2} is {avg}")

#true if a is greater anf flase if a is less
num11=float(input("enter a number:"))
num22=float(input("enter a number:"))
num11,num22
if (num11>=num22):
    print("true")
else:
    print("false")
