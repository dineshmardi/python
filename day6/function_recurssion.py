#function is blocks of code that can be used every time we want to use
#redundant code is not used every time
#tale input and gave some output...input are parameters

def cal(a,b): #we defining how it will work
    sum=a+b
    return sum

cal(3,4)
print(cal(23.4,909))

def hello():
    print("hello")

hello()#if not return than it return none


# average function
def avg_fun(a,b,c):
    return (a+b+c)/3

avg_fun(2,3,4)


#making default valuess
def avg_fun(a,b,c):
    return (a+b+c)/3

avg_fun()#gives error beacause of argument

def avg_fun(a=1,b=1,c=1):
    return (a+b+c)/3

avg_fun()#given default value if argument is not passed

#problems-----
# write a function to print the length of a list 
def fu_len(l):
    return len(l)

a=[1,2,3,4,5]
len(a)

fu_len(a)

# write a function to print the element of a list in a single line.(list as parameter)

def no_list(l):
    i=0
    while(i<len(l)):
        print(l[i],end=" ")
        i+=1


no_list(a)


def facto(n):
    if(n==1 or n==0):
        return 1
    else:
         return n*facto(n-1)

facto(12)


def usd_inr(n):

    inr=n*83
    return inr

print("usd in rupees:",usd_inr(23))

#even odd function

def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")

even_odd(4)
even_odd(9)

#recursion----

def show(n):
    if n==0:#base case
        return
    print(n)
    show(n-1)

show(9)

#write a function to calculate thew sum of first n natural numbers
def summ(n):
    if(n==1):
        return 1
    else:
        return n+summ(n-1)

summ(3)

#write a function that call the list element recursively


# l=[1,2,3,4,5]

# def shh(l,n):
#     if(n==0):
#         return 1
#     else:
#         print(l[n])
#         return l[n-1]

# shh(l,3)


