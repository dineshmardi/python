#use del to delete the object or variable--

class student:
    def __init__(self,name):
        self.name=name

s1=student("dinesh")
print(s1.name)
del s1.name
print(s1.name)#this rase error now

#private (like) attributes andmethods--


class account:
    def __init__(self,acc_no,acc_pass):
        self.__acc_no=acc_no#we cannot accesss outside of class
        self.acc_pass=acc_pass

acc1=account("89678","hgsdf67")
print(acc1.acc_no)#private variable done by __ two underscore..

class person:
    __name="anonymous"
    def __hello(self):#accessed by only within class objects function attributes
        print("hello")
    def welcome(self):
       self.__hello()


p1=person()
print(p1.welcome())


#inheritence----------------
# one class derive the property and method of another class

class car:#base class
    
    def start(self):
        print("car started...\n")
    
    def stop(self):
        print("car stopped\n")


class toyotacar(car):#derived class
    def __init__(self,name):
        self.name=name

car1=toyotacar("fortuyner")
car2=toyotacar("honda")
print(car1.start())

#single inhertance x->y
#multilevel inheritance x->y->z
class car:#base class
    
    def start(self):
        print("car started...\n")
    
    def stop(self):
        print("car stopped\n")


class toyotacar(car):#derived class
    def __init__(self,name):
        self.name=name

class honda(toyotacar):
    def __init__(self):
        print("hello honda family")

car1=toyotacar("fortuyner")

car2=honda()
print(car2.start())

#multiple inheritance  x->y->z<-a<-b

class a:#base
    ca="welcome to a"
class b:#base
    cc="welcome to b"
class d(a,b):#child
    cd="welcom to c"
    
ab=d()
print(ab.ca,ab.cc,ab.cd)


#super method.....to access methiod class that is 
#taking about parents class super() to access parent
class car:
    def __init__(self,type):
        self.type=type
    def start(self):
        print("start....")
    def stop(self):
        print("stop....")
class toyota(car):
    def __init__(self,name,type):
        self.name=name
        # self.type=type() #this is not we want this is type variable inside toyota class
        super().__init__(type)
        super().start()#tto access parent class
        super().stop()


car1=toyota("heroo","electric")
print(car1.type)



#class method...if no attribute or variable inside method then we use @staticmethod
class person:
    name="dinesh"
    def change(self,name):
        self.__class__.name=name#change clas attribute
        #person.name=name  another way

    @classmethod#another way to access class varible rather than instance varible or attribute

    def chanename(cls,name):
        cls.name=name

p=person()
print(p.name)
print(p.change("gyan"))
p.chanename("hariom")
print(p.name)




