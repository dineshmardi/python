#file input and output are here in this code io---input output
#alll thing are just file

# open read close

f=open("/workspaces/python/day6/function_recurssion.py","r")
data=f.read()
print(data)
print(type(data))
f.close()
del data

f.readlines()


f=open("hello.txt","a")
f.write("this is the code to know write in io\n")

#to delete a file we can simply do..import os module that is just like a library and many
# functipon are eriten inside that module
import os
os.remove("hello.txt")



#question on io
#open a file or create and add some data
with open("practice.txt","w")as f:
          f.write("hi everyone\n we are larning fimei/o\n")
          f.write("good")
#we not need towrite f.close() to make it close because it is called automatically when it is called i.e with syntax

with open("practice.txt","r") as f:
        data=f.read()

new_data=data.replace("are","people")
print(new_data)

with open("practice.txt","w") as f:
        data=f.write(new_data)


#finding a word in a file

with open("practice.txt","r") as f:
        data=f.read()
        if(data.find("hi")!=-1):
                print("found\n")
        else:
                print("not found")
