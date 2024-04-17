
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