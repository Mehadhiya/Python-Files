
#example1--teaching
class goa:
    name=""           #variable
    drink=""
    def party(self):  #function(when we use function within class use self keyword)
        print("Lets party....")
    def beach(self):
        print("enjoy the view")
ramesh=goa()   #object
suresh=goa()

ramesh.name="Ramesh"    #assigning value to the variable name and drink for object
print(ramesh.name)
ramesh.drink="yes"
print("drink:",ramesh.drink)

suresh.name="Suresh"
print(suresh.name)
suresh.drink="yes"
print("drink:",suresh.drink)

ramesh.party()      # calling the funtion using object
suresh.beach()

#example2---teaching

class laptop:
    price=0
    processor=""
    RAM=""
hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.processor="i5"
hp.RAM="8GB"

dell.price=60000
dell.processor="intel"
dell.RAM="16GB"

lenovo.price=70000
lenovo.processor="i7"
lenovo.RAM="4GB"

print("Price for hp:",hp.price)
print("Processor for dell:",dell.processor)


#example3 ----teaching
class laptop:
    def __init__(self):     #Constructor (init -->inbuild function)----->when we create the object,the constructor will be automatically created which is used to allocate the memory space
        self.ram="67"
        self.proc="i9"        #The main purpose of the constructor is to initialize or assign values to the data members of the class     
    def display(self):       #Self keyword is denotes the which object is currently used
        print("ram:",self.ram)
        print("processor:",self.proc)
hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.proc="i5"

dell.ram="16gb"
dell.proc="i7"

hp.display()
dell.display()

#To run the empty class we use pass keyword

class laptop():
    pass

#example1 --practical 
class student: 
    def __init__(self):
        self.name=""
        self.reg_no=0
    def display(self):
        print("name:",self.name)   
        print("reg_no:",self.reg_no)
std1=student()

std1.name="ragu"
std1.reg_no=101

std1.display()

#example2---practical
class fruit:
    def __init__(self,col):
        self.color=col
        print("color:",self.color)
apple=fruit("red")

#example3----practical
class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)
t1=teacher("ravi","102")
t2=teacher("seetha","103")
t1.display()
t2.display()

#example4---practical
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
       c=self.a+self.b
       print("addition:",c)
    def sub(self):
       d=self.a-self.b
       print("subtraction:",d)
    def mul(self):
       e=self.a*self.b
       print("multiplication:",e)
    def div(self):
       f=self.a+self.b
       print("division:",f)
cal=calculator(10,10)
cal.add()
cal.sub()
cal.mul()
cal.div()



#Different types of variables in classes
#1.Instance variable--->It is used inside the constructor (If the particular variable value change with the object that time we use this variable)
#2.class variable--->It is used as a global variable on the first declaration of class(If the particular variable value doesnot change with the object that time we use this variable )

#example for instance variable
class phone:
    def __init__(self,price,chargertype):        #Constructor
        self.price=price                        #Instance Variable
        self.chargertype=chargertype            #Instance Variable
    def display(self):
        print("Price:",self.price)
        print("chargertype:",self.chargertype)
vivo=phone(10000,"B-Type")
vivo.display()

redmi=phone(20000,"C-Type")
redmi.display()

#example for class variable
class phone:
    chargertype="C-Type"                         #Class Variable
    def __init__(self,price):                    #Constructor
        self.price=price                         #Instance Variable
    def display(self):
        print("Price:",self.price)
        print("chargertype:",self.chargertype)
vivo=phone(10000)
vivo.display()

redmi=phone(20000)
redmi.display()


#different type of methods in classes(Funtion another name is method)
#Instance Method----wherever the self keyword used with function that method is called instance method
#class Method   ----same as class variable but it is used as a function

#Instance Method 
class laptop:
    def __init__(self):
        self.price=10000
        self.ram="i5"
    def setprice(self,price):    #instance method(self keyword)
        self.price=price
    def getprice(self):
        print("Price:",self.price)
hp=laptop()
hp.setprice(20000)
hp.getprice()
      
#Class Method
class laptop:
    chargertype="C-Type"
    def __init__(self):
        self.price=10000
        self.ram="i5"
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print("Price:",self.price)
    @classmethod                      #Another way to use call the class method(decorator)
    def changechargertype(cls):       #function with class argument
        cls.chargertype="B-Type"
        print("charger type is changed to B")
    @staticmethod                     #This is a decorator used to print or any calculation should not change anywhere
    def info():
        print("This is a class method")
hp=laptop()
hp.setprice(20000)
hp.getprice()
#laptop.changechargertype(laptop)   #one of the way to call the class method 
hp.info()



#Super Keyword----It is used to call the content in constructor of base class or any other class 


class a:
    def __init__(self):
        print("A")
    def dispA(self):
        print("You call class A")
class b():
     def __init__(self):
        super().__init__()        #It calls the content of base class constructor of class A in class B
        print("B")
     def dispB(self):
        print("You call class B")
class c(b,a):
     def __init__(self):
        super().__init__()        #It calls the content of base class constructor of class A in class B
        print("C")
     def dispB(self):
        print("You call class C")
ob1=c()

#when we use multiple inheritance using with super keyword it first call the first denoting of class second one is ignored

#greatlearning oops concept
#class creation
class phone:
    def make_call(self):
        print("You can call here")
    def play_game(self):
        print("Play game here")
vivo=phone()
vivo.make_call()
vivo.play_game()


#class and object using parameter
class phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        print (self.color)
    def show_cost(self):
        print (self.cost)
vivo=phone()
vivo.set_color("yellow")
vivo.set_cost(10000)
vivo.show_color()
vivo.show_cost()

#Class and object with constructor

class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def show_detils(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)
ram=employee("ram",23,20000)
ram.show_detils()