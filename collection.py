''' List      -->It is a collection which is ordered and changeable (mutable)
     Allows Duplicate members
     Any type of data ca be stored
     We can modify the list item. we can add or remove --insert(),append(),extend(),pop()'''
     
a=[1,2,3,4,5]
print(a)
a.append(7)      #(add the value in last column of list)
a.append(79)
print(a)
print(a[1])      #(It shows the value in 1st position of list----1 is the position of second value in list(index start from 0---0,1,2,3,4.....))
a.insert(0,11)   #(0-position in list,11-replacement value ,but value in 0th position is shifted to 1st position not deleted) 
print(a)
a[1]=12         #(It is used to totally replace the particular position value,the already stored value will be automatically deleted)  
print(a)
a.pop(6)        #(It is used to remove (delete)the particular position value in list,If you dont give the position value it remove the last value from list)
print(a)
b=[43,23,45]
a.extend(b)     #(It is used to merge the two list of values)
print(a) 



''' Tuple----> It is a collection which is ordered and unchangeable
               Allow Duplicate members
               Any type of data can be stored
               We cannot modify the tuple item. we cannot add or remove but we can change the type from tuple to list'''


a=(1,2,3,4,5)
b=list(a)
print(a)
print(b)





''' Set------> It is a collection which is unordered and unchangeable and unindexed
               No duplicate members
               Any type of data can be stored
               We cannot modify the set item. but we can add or remove items,  add(),update(),remove(),pop()'''
               

a={1,2,3,4,5,1}    #remove duplicate values
a.add(7) 
print(a)
a.remove(7)        
print(a)  
a.pop()           # every time it change the postion of deletion item
print(a)

a={1,2,3,4,5}
b={3,4,5,6,7}
a.union(b)
print(a)

a={1,2,3,4,5}
b={3,4,5,6,7}
c= (a.intersection(b))
print(c)

         
               
               
''' Dictionary----> It is a collection which is ordered and changeable
                     No Duplicate members,Duplicate value will overwrite existing value
                     Any type of data can be stored
                     Key:value pair {"name":"EMC"}
                     get(),keys(),values(),items(),update({"year":2020}),
                     thisdict["color"]="red",thisdict.pop("model"),del,clear()'''



dict={
     "name":"dhiya",
     "age":22,
     "location":"tirunelveli",
}
print(dict)
print(dict.keys())
print(dict.values())
dict["color"]="red"  #1st way of update 
print(dict)
dict.update({"age":23})  #2nd way of update
print(dict)
#dict.pop("age")  #print(dict)   1st way of delete option
del dict["age"]   #2nd way of delete option
print(dict)
dict.clear()    #clearing the value only empty braces are there
print(dict)

