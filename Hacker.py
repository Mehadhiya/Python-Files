n=int(input())
scores=[]
for i in range(n):
    list_val= input("Enter list Value:")   #scores = list(map(int, input().split()))
    scores.append(list_val)
scores.sort(reverse=True)
runner_up = scores[0]

for score in scores:
    if score < runner_up:
        runner_up = score
        break
print(runner_up)





if __name__ == '__main__':
    N = int(input())
    list_ = []
    for i in range(N):
        command = input().strip()
        command, *values = command.split()
        match command:
            case "insert":
                list_.insert(int(values[0]), int(values[1]))
            case "print":
                print(list_)
            case "remove":
                list_.remove(int(values[0]))
            case "append":
                list_.append(int(values[0]))
            case "sort":
                list_.sort()
            case "pop":
                list_.pop(-1)
            case "reverse":
                list_ = list_[::-1]
                


s = input()
# Initialize flags to track different character types
has_alphanumeric = False
has_alphabetical = False
has_digits = False
has_lowercase = False
has_uppercase = False

# Iterate through each character in the input string
for char in s:
    if char.isalnum():
        has_alphanumeric = True
    if char.isalpha():
        has_alphabetical = True
    if char.isdigit():
        has_digits = True
    if char.islower():
        has_lowercase = True
    if char.isupper():
        has_uppercase = True

# Print the results for each condition
print(has_alphanumeric)
print(has_alphabetical)
print(has_digits)
print(has_lowercase)
print(has_uppercase)


s =  input()
check= False
for s in s:
    if s.isdigit():
        check = True
print(check)        
    
if s.isalnum():
    print("AlphaNumeric")
else:
    print("Not a Alpha Numeric")
    
    
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                coordinates.append([i, j, k])

print(coordinates)




# Read the number of students' records
n = int(input())

# Create a dictionary to store student information
student_data = {}

# Read the student records and calculate the average marks
for _ in range(n):
    record = input().split()
    name = record[0]
    marks = list(map(float, record[1:]))
    average_marks = sum(marks) / len(marks)
    student_data[name] = average_marks

# Read the query name
query_name = input()

# Print the average marks for the query_name with 2 decimal places
print("{:.2f}".format(student_data[query_name]))


# Read the thickness value
thickness = int(input())

# Top Cone
for i in range(thickness):
    print((".|." * i).center(thickness * 3, "-"))

# Welcome Message
print("WELCOME".center(thickness * 3, "-"))

# Bottom Cone
for i in range(thickness - 1, -1, -1):
    print((".|." * i).center(thickness * 3, "-"))





#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



import textwrap
def wrap(string, max_width):
    lines = []
    for i in range(0, len(string), max_width):
        lines.append(string[i:i + max_width])
    return '\n'.join(lines)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
    
def door_mat_design(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome = 'WELCOME'.center(M, '-')
    return '\n'.join(pattern + [welcome] + pattern[::-1])

# Read input
N, M = map(int, input().split())

# Call the door_mat_design function and print the result
result = door_mat_design(N, M)
print(result)



# Initialize two empty 2x2 matrices
A = [[0, 0], [0, 0]]
B = [[0, 0], [0, 0]]
m=int(input("Enter row number for m:"))
n=int(input("Enter column number for n:"))

# Read values for the first matrix A
print("Enter values for matrix A:")
for i in range(m):
    for j in range(n):
        A[i][j] = int(input("Enter the value for A[{i}][{j}]: "))

# Read values for the second matrix B
print("Enter values for matrix B:")
for i in range(m):
    for j in range(n):
        B[i][j] = int(input("Enter the value for B[{i}][{j}]: "))

# Initialize a result matrix C with zeros
C = [[0, 0], [0, 0]]

# Perform matrix addition element-wise
for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]

# Print the result matrix C
print("Result matrix C:")
for row in C:
    print(*row)
