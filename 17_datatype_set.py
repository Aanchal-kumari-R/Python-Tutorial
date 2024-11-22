fd = {None} 
print(type(fd))   

#Dictionary 
fd= set({11,22,22.5, 2+3j ,"Mohan",11,22,"Mohan","Ram"})
print(fd)

fd1= {11,22,22.5, 2+3j ,"Mohan",11,22,"Mohan","Ram"}
print(fd1)   

#length 
print(len(fd1))  

#Union  
# The union() method returns a new set with all items from both sets.
n1 = {11,22,33,44}
n2 ={55,66,11,22,44}
print(n1.union(n2))  

#Difference
print(n1.difference(n2))  

#intersection   
print(n1.intersection(n2))   

#Add Items
thisset = {"apple","banana","cherry"} 
thisset.add("mango") 
print(thisset)   
print(thisset.update("Papaya")) 
print(thisset)  

#Remove Set Items  
thisset = {"apple","banana","cherry","papaya","Guava"}  
thisset.remove("banana") 
print(thisset)   


thisset.discard("cherry") 
print(thisset) 

x = thisset.pop() 
print(x)  

thisset.clear() 
print(thisset)  

#Loop Items 
 
myset = {"apple","banana","cherry","papaya","Guava"} 
for x in myset: 
    print(x)   

myset = {"apple","papaya","Guava"} 
thisset = {"apple","pineapple","cherry","papaya"}  
myset.update(thisset) 
print(myset)  

x =  {"apple","papaya","Guava"}  
y = {"google","microsoft","apple"} 
x.intersection_update(y) 
print(x)  

x.symmetric_difference_update(y) 
print(x) 

z = x.symmetric_difference(y) 
print(z)  

x =  {"apple","papaya","Guava"}  
y = {"google","microsoft","facebook"} 
z = x.isdisjoint(y) 
print(z)  

x = {"a","b","c"}  
y = {"f","e","d","c","b","a"} 
z = x.issubset(y) 
print(z)  

y = {"f","e","d","c","b","a"} 
x = {"a","b","c"}  
z = x.issuperset(y) 
print(z)  

y = {"f","e","d","c","b"} 
x = {"a","b","c"}  
z = x.issuperset(y) 
print(z)



   






