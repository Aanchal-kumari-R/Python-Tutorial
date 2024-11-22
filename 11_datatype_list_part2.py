 #List comprehension 
fruits = ["apple","banana","mango","Kiwi","cherry"] 
newlist =[]  

for x in fruits:    
    if "a" in x: 
        newlist.append(x) 
print(newlist) 

fruits = ["apple","banana","mango","Kiwi","cherry"]  
newlist = [x for x in fruits if "a" in x] 
print(newlist)  

fruits = ["apple","banana","mango","Kiwi","cherry"] 
newlist = [x for x in fruits if x != "Kiwi"] 
print(newlist)  

fruits = ["apple","banana","mango","Kiwi","cherry"] 
newlist = [x for x in fruits] 
print(newlist)  

newlist = [x for x in range(10)]     
print(newlist)

newlist = [x for x in range(10) if x <5] 
print(newlist)  

fruits = ["apple","banana","mango","Kiwi","cherry"] 
newlist = [x.upper() for x in fruits]  
print(newlist)    

fruits = ["apple","banana","mango","Kiwi","cherry"] 
newlist = ["hello" for x in fruits] 
print(newlist)    

df1 = [11,22,33,44,55,66,77,88] 
num2 = ["Even number" if df1[i] %2==0 else "Odd number" for i in range(len(df1))] 
print(num2)

fruits = ["apple","banana","mango","Kiwi","cherry"] 
newlist = [x if x != "banana" else "orange" for x in fruits] 
print(newlist)  
 
#Sorting 
fruits = ["apple","banana","mango","kiwi","cherry"] 
fruits.sort() 
print(fruits)  

thislist = [12,3,5,67,788,99] 
thislist.sort() 
print(thislist)  

fruits = ["apple","banana","mango","kiwi","cherry"] 
fruits.sort(reverse=True) 
print(fruits)  
 
thislist = [12,3,5,67,788,99] 
thislist.sort(reverse=True) 
print(thislist)  

#copy the lists   
fruits = ["apple","banana","mango","kiwi","cherry"] 
thislist = fruits.copy() 
print(thislist)  

thislist = [12,3,5,67,788,99] 
newlist = list(thislist) 
print(newlist)  

#Join list  
fruits = ["apple","banana","mango","kiwi","cherry"] 
thislist = [12,3,5,67,788,99] 
newlist = fruits+thislist 
print(newlist) 

fruits = ["apple","banana","mango","kiwi","cherry"] 
thislist = [12,3,5,67,788,99] 
for x in thislist: 
    fruits.append(x) 
    print(fruits)
 
fruits = ["apple","banana","mango","kiwi","cherry"] 
thislist = [12,3,5,67,788,99] 
thislist.extend(fruits) 
print(thislist)  

thislist = [12,3,5,67,788,99] 
print(4*thislist)  

df1 = [2,3,4,5] 
df2 = df1  
df3 = df1[:] #Cloning
print(df1) 
print(df2) 
print(df3)  

#Memory Allocation
print(id(df1)) 
print(id(df2)) 
print(id(df3))  

df1.append(7)  
print(df1)   
print(df2) 

df2.append(4) 
print(df2)   
print(df1)  
 
df3.append(8) 
print(df3) 
print(df1)  
print(df2)  





