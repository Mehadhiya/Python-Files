# It is used to avoid the variable usage in private .Once it changed to Private variable only accessible within the class Not outside the class.(security purpose)
#example---theory   (to restrict the access and hide the data called encapsulation)(ACCESS MODIFIERS--->__private,company-public,_protectod)

class company:
    def __init__(self):                 
        self.__companyname="Google"     #private
    def companyname(self):              #public
        self.__companyname="Goooogle"
        print(self.__companyname)
c1=company()
c1.companyname()



#protected variable ---it is used in the inherited class also 

class company:
    def __init__(self):
        self._companyname="Google"
class b(company):               #inherited class use variable
    pass
b1=b()
print(b1._companyname)

############################################################################################################
#Three types of errors: 1)Compile time error(syntax error)    2)logical error  3)runtime error

print("hai")
#printt("hello")              #It give the name error during compilation time


a=10
b=20
print(a+a)                   # it does not give error,it run but in logical term present the error

a=int(input())
b=int(input())
print(a+b)                   #it give the error when the user input is not match with the program datatype during runtime


#Exceptional Handling-----To rectify the runtime error we use this handling method(User mistake)
try:
    a=int(input())
    b=int(input())
    print(a+b)
except Exception as e:
    print("Something",e)       #e specify the what type of error in try block

try:
    a=int(input())
    b=int(input())
    c=input()
    print(c/a)
    #print(d)
except ValueError as e:                    #It rectify only this type of error come otherwise it throw error
    print("value error:",e)
except TypeError as e:
    print("Type error:",e)
except Exception:
    print("Somethimg Wrong")
finally:                               #With or without error this block automatically executed
    print("Done")
