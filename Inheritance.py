#Single Inheritance-----One base class is used with another one class (function and variables) called single inheritance
#example--theory

class dad():                     #1st class
    def phone(self):
        print("Dad's Phone")
class son(dad):                  #2nd class   ---which is linked to 1st class using dad keyword
    def laptop(self):
        print("Son's Laptop")
ram=son()                        #object created for 2nd class
ram.phone()                      #2nd class object access the 1st class function or anything
    
    
#Multiple inheritance ------Many base class is used with one classes(functionand variables) called multiple inheritance
#example---theory

class dad():                     #1st class
    def phone(self):
        print("Dad's Phone")
        
class mom():                    #2nd class
    def sweet(self):
        print("Mom preparing sweet for Son")
        
class son(dad,mom):              #3rd class   ---which is linked to 1st class  and 2nd class using dad  and mom keyword
    def laptop(self):
        print("Son's Laptop")
ram=son()                        #object created for 3rd class
ram.phone()                      #3rd class object access the 1st class function or anything
ram.sweet()                      #3rd class object access the 2st class function or anything


#multilevel Inheritance   ---many base classes linked to many classes or vice versa 
#example---theory

class grandpa():                    #1st class
    def phone(self):
        print("Grandpa's Phone")
    
class dad(grandpa):                 #2nd class linked to 1st class
    def money(self):
        print("Dad's money")

class son(dad):                     #3rd class linked to 2nd class   (But the 3rd class is accessabile for both 2nd and 1st class because of 2nd classes linked with 1st class)
    def laptop(self):
        print("Son's laptop")

ram=son()                           #object creation for 3rd class
ram.money()                         #3rd object access the 2nd function
ram.phone()                         #3rd object access the 1st function

ragu=dad()                          #object creation for 2nd class
ragu.phone()                        #2nd object access the 1st function

#Heirarchical Inheritance        -----one base class which is used by many classes
#example---theory

class dad():              #base class
    def money(self):
        print("Dad's Money")
class son1(dad):         #derived class 1 linked to base class
    pass
class son2(dad):         #derived class 2 linked to base class
    pass
class son3(dad):         #derived class 3 linked to base class
    pass

s2=son2()               #object creation for derived class 2
s2.money()              #2nd object access the base class

#Hybrid Inheritance -----Combination of Single,Mulitiple,Multilevel and heirarchial inheritance
#example---theory

class dad():              #base class
    def money(self):
        print("Dad's Money")
class land():             #another base class
    def info(self):
        print("Important Land")
class son1(dad):         #derived class 1 linked to base class
    pass
class son2(dad,land):         #derived class 2 linked to base class and another base class
    pass
class son3(dad):         #derived class 3 linked to base class
    pass

s2=son2()               #object creation for derived class 2
s2.money()              #2nd object access the base class
s2.info()               #2nd object also access the another base class
               #This program used multiple and heirarchial inheritance
               


#single inheritance

class vehicle:
    def __init__(self,mileage,speed,hp):
        self.mileage=mileage
        self.speed=speed
        self.hp=hp
    def show_details(self):
        print("mileage:",self.mileage)
        print("speed:",self.speed)
        print("horse power:",self.hp)
class car(vehicle):
    def show_car(self):
        print("details of the car")
car2=car(100,40,500)
car2.show_car()
car2.show_details()


#single inheritance with overriding constructor
class vehicle:
    def __init__(self,mileage,speed,hp):
        self.mileage=mileage
        self.speed=speed
        self.hp=hp
    def show_details(self):
        print("mileage:",self.mileage)
        print("speed:",self.speed)
        print("horse power:",self.hp)
class car(vehicle):
    def __init__(self,mileage,speed,hp,cost):
        super().__init__(mileage,speed,hp)
        self.cost=cost
    def show_car(self):
        print("details of the car")
        print("cost of the car:",self.cost)
car2=car(100,40,500,1000000)
car2.show_car()
car2.show_details()


#multiple inheritance
class parent1:
    def str1(self,str1):
        self.str1=str1
    def show_str1(self):
        print(self.str1)
class parent2:
    def str2(self,str2):
        self.str2=str2
    def show_str2(self):
        print(self.str2)
class child(parent1,parent2):
    def str3(self,str3):
        self.str3=str3
    def show_str3(self):
        print(self.str3)
ch1=child()
ch1.str1("hello")
ch1.str2("world")
ch1.str3("Beautiful day")
ch1.show_str1()
ch1.show_str2()
ch1.show_str3()

#multilevel inheritance

class parent:
    def name(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
class child(parent):
    def age(self,age):
        self.age=age
    def show_age(self):
        print(self.age)
class grandchild(child):
    def salary(self,salary):
        self.salary=salary
    def show_salary(self):
        print(self.salary)
anu=grandchild()
anu.name("ragu")
anu.age(39)
anu.salary(10000)
anu.show_name()
anu.show_age()
anu.show_salary()