a="Hello, World!"
print(len(a))      # it return the length of string
print("," in a)     # it return true given word is present in string
print("," not in a)  # it return true given word is not present in string
print(a.strip())   #remove the white space in a string
print(a.upper())   # it converts the total string in uppercase format
print(a.lower(),a.casefold())   #it converts the total string in lowercase format (casefold is most effective than lowercase function)
print(a.replace('l','j')) #it replace the string from one to another for every occurance
print(a.split(" "))      #it split the whole string into substring
print(a[1:5],a[:7],a[1:],a[-5:-1])   #slicing string

age = 36
a= "my name is John, and I am {}"
print(a.format(age))      #it is used to insert numbers into strings
print(a.capitalize())     #The first character is converted to upper case, and the rest are converted to lower case

a= "I\tlove apple fruit."
print(a.center(100))      #centre(length,character)---length -->Required. The length of the returned string,character-->Optional. The character to fill the missing space on each side. Default is " " (space)
print(a.count("apple"))   #Return the number of times the value "apple" appears in the string
print(a.endswith("fruit.")) #The endswith() method returns True if the string ends with the specified value, otherwise False.
print(a.expandtabs(30))     #The expandtabs() method sets the tab size to the specified number of whitespaces.
print(a.find("a"))       #The find() method finds the first occurrence of the specified value.returns -1 if the value is not found.The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
print(a.index("a"))   #The index() method finds the first occurrence of the specified value.raises an exception if the value is not found.The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.
print(a.isidentifier())   #A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print(a.istitle())        #The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.Symbols and numbers are ignored.

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)           #The join() method takes all items in an iterable and joins them into one string.

txt = ",,,,,ssaaww.....banana"
print(txt.lstrip(",.asw"),txt.rstrip(",.asw")) #The lstrip() method removes any leading characters (space is the default leading character to remove)

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))  #The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)            #The partition() method searches for a specified string, and splits the string into a tuple containing three elements.The first element contains the part before the specified string.The second element contains the specified string.The third element contains the part after the string. 
print(txt.rfind(all),txt.rindex(all)) #The rfind() method finds the last occurrence of the specified value.returns -1 if the value is not found.
print(txt.swapcase()) #The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
print(txt.title())  #The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
print(txt.zfill(20)) #The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.If the value of the len parameter is less than the length of the string, no filling is done.
print(txt.ljust(20),txt.rjust(20))  #The ljust() method will left align the string, using a specified character (space is default) as the fill character.

#same for sentences---it return output as true or false

a.isalnum()
a.isalpha()
a.isascii()
a.isdecimal()
a.isdigit()
a.islower()
a.isnumeric()
a.isprintable()
a.isspace()
a.isupper()
