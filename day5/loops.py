#loops practice

import time

for i in range(1,6):
    print("hello")

i=1
while(i<5):  #iteration and i is iterator
    print(5)
    i+=1

#printing 1 to  100
while(i<=100):  #iteration and i is iterator
    print(i)
    i+=1
i=100
while(i>=1):  #iteration and i is iterator
    print(i)
    i-=1


#printing table
i,n=1,5
while(i<=10):
    print(n,"*",i,"=",i*n)
    i+=1


for i in [2,3,4,5]:
    j=1
    while(j<=10):
        print(i,"*",j,"=",i*j)
        j+=1
    print("\n")

l=tuple([1,4,9,14,56,78,43,3])
type(l)

for i in l:
    if(i==14):
        print("found ant position:",l.index(i))
        break
    else:
        continue
        # time.sleep(1)
        # print("searching...")
else:#used after complting the loop
    print("end")
#here for is used maximum in datatypes
# and while for indexing typ[type




# methods
for i in range(4):
    print(i)

seq=range(5)#type range
seq
type(seq)

#pass that is null statement
while(true): #this need some codeblocks inside loop

print("hello")


#if we dont want to o anying inside code than w just use PASS statement inside loop


while(true):
    pass#placeholder for future used
print("hello")


#sum of n numbers
sum=0
for i in range(1,6):
    sum+=i
    #pass
sum


#factorial
fact=1
for i in range(1,6):
    fact*=i
    #pass
fact
