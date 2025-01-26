# to map with real world scenario we using objects
# thats called object oriented programming

# to increase reusablity we use oops 
# object and class
# object define the class...class is just a blueprint..what a object should have...ralavent 

class Student:
    name="karan kumar"

s1=Student()#object
print(s1)

s1.name


class car:
    color="blue"
    model="bmw"

car1=car()
car1.color
car1.model


# we are learning about CONSTRUCTOR now..
# here we basically mean a initialliser ok....
# that are defined within class likke __init___(self)...this is default constructor
# and constructor are called when object of a class is initiated...
# constructor are of different type---1.default construtor __init__(self)
# and 2.parameterised constructor --__init__(self,name,name2)

class game:
    def __init__(self):
        print("welcome ",self)

a=game()


class hood:
    def __init__(self,name,gam):
        self.name=name
        self.gam=gam
        print(name,gam)

b=hood("dinesh","vikes")
print(b.gam)

class hero:
    def __init__(self,a):
        self.hero=a
h=hero("krish")
h.hero

#method or functioninside class

class hero:
    def __init__(self,a):
        self.hero=a

    def welcome(self):
        print("hello")
h=hero("krish")
h.hero
h.welcome()


#class that take input as argument and give average of that input 

class student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
  
    def average(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        return avg
    
s=student("dinesh",78,90,65)

print(s.average())

#or


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
      
    def average(self):
       self.sum=0
       for i in self.marks:
           self.sum+=i
           
s=student("dinesh",[12,34,53])
s.average()
print("average=",s.sum/3)




class car:
    def __init__(self):
        self.acc=False
        self.brk=True
        self.clutch=False
        
    def start(self):
        self.clutch=True
        self.acc=True
        print("startedd....")
        
car1=car()
car1.start()
        
           
class amount:
    def __init__(self):
        self.balance=10000
        self.account_no=987865
    def credit(self,money):
        self.balance+=money
        print(money," credeted to you ....available balance=",self.balance)
    def debit(self,income):
        pa=int(input("enter account number="))
        if pa==self.account_no: 
            self.balance-=income
            print(income,"got debited from your account..available balance=",self.balance)
        else:
            pass
        
a=amount()
a.credit(100)
a.debit(1266)


