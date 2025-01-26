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