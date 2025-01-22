#list 

marks=[12,32,32,45,54]
marks
marks[0]
len(marks)
marks[1]="dinesh"
marks 
# list are mutable

#slicing possible

marks[:4]
marks[-len(marks):]

#list function or methods
mar=[1,6,2,8,4,6]
marks.append(9)
mar.sort(reverse=True)#sort but doest show
mar

mar.reverse()  #reverwse from left to right and vice-verse

mar

marks.insert(1,"binod")#insert item at particular position with dleleting that postion element
marks

marks.remove(1)#it remove the element passed in remove ...first occurance is deleted

marks.pop(1)#delete at particular position and return that element

marks
type(marks)

#tuples---

x=tuple(marks)
x
x[4]
x[4]=4#not allowed because it is immutable tuple are immutable


tup=(1)
type(tup)#this shows as integer
tup=(1,)#here it shows tuple fpor single element

type(tup)
 #tuple slicing

x[1:4]

#tuple function or method

x.index(54)#return the index of entered element 
x.count(54)#return the nu m ber of elements present in the tuple


#write a program to enter three favourite movies and store in them in the list
movies=[]
i=0
while(i!=3):
    movies.append(input("enter your favourite movie name:"))
    i=i+1
print(movies)

#write a program to check whether  a list contain palindrome of elements 
list=[1,2,3,4,3,2,1]

list1=list.copy()
list1.reverse()
if (list==list1):
    print("palindrome")
else:
    print("not a palindrome")


#count the grade
grade=("c","d","a","a","b","b","a")
print("number of grade with A:",grade.count("a"))

grade_list= list(grade)#why but converting to list not working
grade_list
grade_list.sort()
grade_list

del list
grade=("c","d","a","a","b","b","a")
list(grade)
grade