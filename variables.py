# variables-to store the value 

a=10
b=10
print(a+b)

# data type-it shows the different type of names 

a="dhiya"
print(type(a))

# operators (=,+,-,*,/) 

a=10
b=20
c=a+b
print(c)

# casting- converting one datatype to another datatype (==int datatype change the string value into integer datatype this is called casting ===)

a=int("10")
b=int("10")
c=a+b
print(c)

# get inputs from user

a=int(input())
b=int(input())
c=a+b
print(c)

# get name and age from user print like a sentence

name=input()
age=int(input())
area=input()
print("My name is:",name)
print("My age is:",age)
print("Area is:",area)

# get integer input for variable a,b,c multiply all 3 variables,add all 3 variables,divide the multiplied value by added values

a=int(input())
b=int(input())
c=int(input())
mul=a*b*c
add=a+b+c
div=(mul//add)
'''print("multiply value:",mul)
print("addition value:",add)'''
print("division value:",div)

# get input for variable name,score,dept,get score for 100,divide 100/10

name=input()
score=int(input())
dept=input()
print("My name is:",name)
print("My score is:",score/10,"/10")
print("My dept is:",dept)


# boolean values-- it first show the true condition print statement

if(True):
    print("yes")
else:
    print("No")
    
# Comparision Operator with if,if-else,nested-if,elif statement 
# example1--if-else with direct input

if("win"=="winn"):
    print("true")
else:
    print("false")
 
#example2 --if-else with user input  
fruit=input("mango or apple?")
if(fruit=="mango"):
    print("I want a juice")
else:
    print("I dont want juice")

#example3---divisible or not with binary operator(and ,or)

num=int(input("give a number:"))
if(num%3==0 and num%5==0):
   print("the number is divisible by 3 and 5")
else:
    print("the number is not divisible by 3 and 5")
    
# example4---even or odd

num=int(input("give a number:"))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")
    
#example5---elif statement

score=int(input("Enter a score out of 100:"))
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("Average student")
elif(score>70 and score<100):
    print("Good student")
else:
    print("Invalid score")
    
#example6---elif statement mini calculator

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
operation=input("add/sub/div/mul:")
if(operation=="add"):
    print("The addition result is:",a+b)
elif(operation=="sub"):
    print("The subtraction result is:",a-b)
elif(operation=="mul"):
    print("The multiply value is:",a*b)
elif(operation=="div"):
    print("The division value is:",a/b)
else:
    print("Invalid operation")
    
#example7---input with input

score=int(input("Enter score value out of 100:"))
if(score>=70):
    name=input("Enter name:")
    age=input("Enter age:")
    location=input("Enter location:")
    print("You are eligible")
else:
    print("you are not eligible")
    
#example8--nested if

salary=int(input("Enter salary:"))
age=int(input("Enter age:"))
if(salary>=20000 or age<=25):
    loan_amount=int(input("Enter amount:"))
    if(loan_amount>=50000):
         print("maximum loan amount is 50000")
    else:
         print("you are eligible for loan")
else:
    print("you are not eligible for loan")


#example9---average mark with if condition

sub1=int(input("Enter sub1 mark:"))
sub2=int(input("Enter sub2 mark:"))
sub3=int(input("Enter sub3 mark:"))
sub4=int(input("Enter sub4 mark:"))
sub5=int(input("Enter sub5 mark:"))
add=sub1+sub2+sub3+sub4+sub5
avg=add/5
if(avg<35):
    print("Additional class is required")
else:
    print("you are good to go:",avg)

# for loop concept---this concept always start from 0 value(It is usually used when the number of iteration is known)
# normal for loop
for i in "orange":
    print(i)

# range for loop
for i in range(10):
    print(i)

for i in range(10,15):
    print(i)
   
#example1---2table using for loop
for i in range (1,11):
    print(i,"x 2 =",i*2)
    
#example2---print the number between two numbers
a=int(input("a:"))
b=int(input("b:"))
for i in range (a+1,b):
    print(i)
 
#example3---print even number between two numbers with count
a=int(input("a:"))
b=int(input("b:"))
e_count=0
o_count=0
for i in range(a,b):
    if(i%2==0):
        print(i)
        e_count=e_count+1
    else:
        o_count=o_count+1
print("Total even count:",e_count) 
print("Total odd count:",o_count)  

#same as examp3----but both odd and even count between two numbers
a=int(input("a:"))
b=int(input("b:"))
e_count=0
o_count=0
for i in range(a,b):
    if(i%2==0):
        print(i)
        e_count=e_count+1
print("Total even count:",e_count) 
for i in range(a,b):
    if(i%2!=0):
        print(i)
        o_count=o_count+1
print("Total odd count:",o_count)  

#example4--count the number which are divisible by 3 and 5 range 1-100

a=int(input("a:"))
b=int(input("b:"))
d_count=0
for i in range (a,b):
    if(i%3==0 and i%5==0):
        print(i)
        d_count=d_count+1
print("Total count for divisible 3 and 5:",d_count)

#For loops with list
#example1---sum of first five natural numbers
a=int(input("a:"))
b=int(input("b:"))
sum=0
for i in range(a,b):
    sum=sum+i
print("The sum of 5 natural number:",sum)
################################
a=int(input("a:"))
b=int(input("b:"))
sum=0
for i in range(a,b):
    sum=sum+i
    avg=sum/10
print("The sum is:",sum)
print("The avg is:",avg) 

#read 10 numbers find their sum and avg(To store the collection of values with different data type -use list)
#list
a=[]
usr=int(input("How many number you want?:"))
for i in range(usr):
    val=int(input("Enter number"+str(i+1)+":"))
    a.append(val) 
print(a)
sum=0
for i in a:
    sum=sum+i
    avg=sum/usr
print("The sum is:",sum)
print("The avg is:",avg)

#print cube number
a=[]
usr=int(input("How many number you want?:"))
for i in range (usr):
     val=int(input("Enter number"+str(i+1)+":"))
     a.append(val)
for i in a:
    cube=i*i*i
    print("The cube value is:",cube)
    
#nested for loop
for i in range(1,3):
     print("week:",i)
     for j in range(1,4):
         print("Day:"+str(j))

#pattern code in number using nested loop(forward number and pattern code)
for i in range(1,10):
    for j in range(1,i+1):
        print("*",end="")  #(print(j,end=""))
    print()

#(reverse number and pattern code)    
n = int(input("Enter num :"))
for i in range(0,n):
    for j in range(0,n-i):
        print(j,end="")    #print("*",end="")
    print()

#while loop(It is usually used when the number of iteration is unknown)

i=0
while(i<5):
    print(i)
    i=i+1
    
i=10
while(i<=200):
    print(i,end=" ")
    i=i+10
    
i=10
while(i>0):
    print(i,end=" ")
    i=i-1
    
#factorial of a number
i=int(input("which number's factorial you want?:"))
num = i
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print("The factorial of "+str(num)+" is:",fact)

#tuple in if statement

tup=(5,10,20.50)
n=int(input("Enter the value:"))
if n in tup:
    print("It is prsent in tuple")
else:
    print("Not present in tuple")
    
#list in if statement

ls=[10,20,30,40]
if ls[1]==20:
    ls[1]=ls[1]+80
    print(ls[1])
else:
    print(ls[1]+ "is not equal to 20")
print(ls)

#dictionary in if statement

dict={"a":10,"b":20,"c":30}
if dict["a"]==20:
    dict["a"]=dict["a"]+100
    print(dict)
else:
    dict["a"]=dict["a"]+150
    print(dict)
    
#list in while loop

ls=[1,2,3,4,5]
i=0
while i<len(ls):
    ls[i]=ls[i]+100
    i=i+1
print(ls)

#list in for loop

ls1=["red","green","yellow"]
ls2=["mango","papaya","apple"]
i=0
for i in ls1:
    for j in ls2:
        print(i,j)

# reverse the number

n=int(input("Enter a number:"))
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig 
    n=n//10
print("The reverse number is:",rev)

#palindrome 

n=int(input("Enter the number:"))
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print(str(temp)+" number is palindrome")
else:
    print(str(temp)+" number is not a palindrome")

#fibonacci series

n=int(input("Enter the number:"))
a=0
b=1
if n==0:
    print(a)
elif n==1:
    print(b)
else:
    for i in range (2,n):
        c=a+b
        a=b
        b=c
    print(b)

        
