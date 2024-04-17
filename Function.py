#calculator using function

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
def add():
    print("The addition value is:",a+b)
def sub():
    print("The subtraction value is:",a-b)
def mul():
    print("The multiplication value is:",a*b)
def div():
    print("The division value is:",a/b)
add()
sub()
mul()
div()

#Even or add the value is getting from user---parametrized function

n=int(input("Enter number:"))
def oddeven(num):
    if(num%2==0):
        print("Given number is even")
    else:
        print("Given number is odd")
oddeven(n)

#print the range from a to b which input is get from user

def printrange(a,b):
    for i in range(a,b):
        print(i)
n1=int(input("Enter n1 value:"))
n2=int(input("Enter n2 value:"))
printrange(n1,n2)


#return keyword 
#example1--sample
def a():
    return 20
n=a()
print(n)
print(a())

#example2
s_usrname="dhiya"
s_password="1234"
usrname=input("Enter value for username:")
password=input("Enter value for password:")
def validate():
    if(s_usrname==usrname and s_password==password):
         return True
    else:
        return False
a=validate()
print(a)


#example3   (a+b)*c using return 
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
def add():      #def add(a,b)
    tmp=a+b     #return a+b
    return tmp  #added=add(a,b)
d=add()         #output=added*c
print(d*c)      #print(output)


#lambda function  -A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.
def myfun(n):
    return lambda a:a*n
double=myfun(2)
print(double(11))  


#count of the particular string in origial string
def count_substring(original_string, substring):
    count = 0
    sub_len = len(substring)
    
    for i in range(len(original_string)):
        if original_string[i:i + sub_len] == substring:
            count += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count) 
    
#lambda function with filter

ls=[1,2,3,10,78,29,78]
ls1=list(filter(lambda x:(x%2!=0),ls))
print(ls1)

#lambda functions with map

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 

from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 