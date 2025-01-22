#string declaration 
str1="string"
str2='string'
str3='''string'''
print(str3)

#escape sequence

str="hello this dinesh\nand this is my second day code"
str

#concatenation
concate=str1+" "+str2#space is also counted and spcial charater also counted
concate
len(concate)

#indexing
concate[0]
concate[len(concate)-1]

str[5]="@"
#slicing in string python

concate[0:12:2]#strat stop steep
concate[:12:2]
concate[:12:]
concate[2:]
concate[::2]
concate[-len(concate):]

#string function

concate.endswith("g")
concate.capitalize()#no change in previous variable
concate.replace("s","t")
concate.find("g")#find index of g that is starting g in the 
concate.count("s")#count the number of string

#write a program to inp[ut user name and print its length
name=input("enter your name=")
print("the length of your name is=",len(name))

#write a program to find the occurance of "$" in a string
if(name.find("$")==-1):
    print("no")


#CONDITIONAL STATEMENTS
a=8
b=4
c=6
if((a>b)&(a>c)):
    print(a,"a is greater.")
elif((a>b)&(a<c)):
    print(a,"is greater than c")
elif((b>a)&(b>c)):
    print("b greater")
else:
    print("c is greater")

#NESTING    
age=67
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("hello noob")


#write a program to check if a number entered by the user is odd or ven
num=int(input("enter a number="))
if(num%2==0):
    print("even")
else:
    print("odd")

#find the greatest of three number input by the user
num1=int(input("enter a number="))
num2=int(input("enter a number="))
num3=int(input("enter a number="))

if(num1>num2 and num1>num3):
    print("num1 is greater")
elif(num2>num3):
    print("num2 is greate")
else:
    print("num3 is greater")

#check multiple of 7

num=16
if(num%7==0):
    print("divisible by 7")
else:
    print("not a multple of 7")