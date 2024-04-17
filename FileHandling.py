#File Handling need two files to access one is python file(.py) and another one is text or any file(here Filehandling.py and demo.txt files are used)

#Open and read the file
f=open("demo.txt")        #open the file 
content=f.read()          #read the file (default mode is read if you want to change the mode you will be specify like this("example.txt","w"---->it overwrite the existing data with user given data) or ("example.txt","a"-->append the new data which is written by user) or ("example.txt","r+"-->it perform read and write operation together))
print(content)

#open and write the file 
f=open("demo.txt","w")
f.write("This is my first file handling")
f.close()  #Every write function need close() function without this,it will not work

f=open("demo.txt","r")
content=f.read()
print(content)

#open and append the data in file
f=open("demo.txt","a")       #append the data to the file
f.write("\nApple\n")
f.write("Orange\n")
f.write("Mango")
f.close()

f=open("demo.txt","r")
content=f.read()
print(content)