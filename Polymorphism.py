#Polymorphism--->It means the same function name being used for many types.The Key difference is the data types and number of arguments used in function
#example---theory

def add(a,b,c=0):
    print(a+b+c)        #Here the same add function call 2 times with different parameter the default parameter is set when noone value is given to particular parameter 
add(1,2)
add(1,2,3)


#method Overriding----It replace the one function value from another function value
#example using inheritance with method overriding
                                                 #multilevel inheritance
class Animal():                    
    def sound(self):
        print("Animal Makes Sound")       #normal function

class Dog(Animal):
    def sound(self):
        print("Dog Barks")                #the function in base class which is used for different purpose with same name in derived class (ie)Overriding the function 

class Bird(Animal):
    def sound(self):
        print("Birds Sing")
        
Animal1=Dog()
Animal1.sound()

Animal2=Bird()
Animal2.sound()


#example1---Practical

class shape():
    def area(self):
        return 0
class rectangle(shape):       #Single Inheritance with method overriding
    def area(self):
        l=10
        b=20
        print("Area of rectangle:",l*b)
area1=rectangle()
area1.area()

#example2---practical

class person():                     #Single Inheritance
    def __init__(self,name):        #constructor parameter   
        self.name=name
class student(person):              
    def __init__(self,name,grade):   #constructor parameter
        super().__init__(name)     #calling the another or base class constructor
        self.grade=grade
    def display(self):
        print(self.name,self.grade)
stud1=student("Ragu","A")       #object creation
stud1.display()               #calling the function

#example3---practical

class vehicle():          #single inheritance with method overriding
    def start(self):
        print("Vehicle Started")
class car(vehicle):
    def start(self):
        print("Car started")
access=car()
access.start()
    
    
#example4---practical

class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print(self.name,self.salary,self.department)
Man1=Manager("Ragu",20000,"CSE")
Man1.display()
        