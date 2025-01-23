#dictionary----
dict={"name":"dinesh","age":23,"village":"hartopa"}
dict
print(dict)
dict["name"]

dict["name"]="amar"
dict
dict["surname"]="mardi"
dict

#nested dictionary
student={}#empty dictionary
student["name"]="dinesh"
student["sub"]={"phy":56,
                "che":67,
                "maths":99}
student["sub"]["phy"]


#dict methods
student.keys()
list(dict.keys()) #type cast tolist


dict.values()
student.values()

student["name2"]#throw error
student.get("name2")#doesnt theow error

#if it is possible that particular block will throw error than use try cath or methods to avoid he error throw for not interrupting the code
student.update({"class":12,"hod":"amrnath"})
student#update function to update the existing dictionary


#sets--
#all set are immutable and unique

num={1,2,3,4,}
num
num1={1,2,3,4,4}#set are unique
num1

#dictionary and list are not accepted in set as thery are mutable...tuple is accepted

a=set() #wmpty set
a
type(a)
type(num)

#set methods
a.add(("dinesh","mardi","1"))
a
type(a)
#set are mutrable but elements are immutable

a.remove("dinesh")


a.clear()
a#to cleara set

a
a.pop()
a

a={1,2,3,4,5}
b={3,4,5,6,7,8}
a.union(b)
a.intersection(b)#common values

#store in dictionary
name={"table":["a piece of furniture","list of facts and figures"],"cat":"a small animal"}
name.values()
list(name.keys())


#classrooms required

sub=["python","java","c++","python","javascript","java","python","java","c++","c"]
sub
uni=set(sub)
print("the number of class required=",len(uni))

#write a program to enter marks of 3 subjects form the user and store them in the dictionary
#start with the empty dictionary and add one bby  one .use subject name as key and marks as value

dictionary={}
dictionary["maths"]=int(input("enter maths marks="))
dictionary["science"]=int(input("enter marks of science:"))
dictionary["english"]=float(input("enter the marks of english:"))

print(dictionary)

x=set(dictionary)
x={9,float(9.0)}
x#9a nd 9.0 are treated same

x={9,"9.0"}
x