#Blank set 
myset = {None} 
print(type(myset))  

myset = {} 
print(type(myset))  

myset = {"apple","banana","cherry"} 
print(myset)  
 
#Duplicate value not allowed 
myset = {"apple","banana","cherry","apple"} 
print(myset) 

#True and 1 are same so only one can print
myset = {"apple","banana","cherry","apple",True,1,0} 
print(myset)  

#False and 0 are same so only one can print 
myset = {"apple","banana","cherry","apple",True,1,0,False} 
print(myset)   

#length of a myset 
myset = {"apple","banana","cherry","apple",True,1,0,False} 
print(len(myset))  

set1 = {"abc", 34, True, 40, "male"}
print(set1)  

#set Constructor 

myset = set(("apple","banana","cherry")) 
print(myset)  

#Access items 
myset = {"apple","banana","cherry"} 
for x in myset: 
    print(x) 

myset = {"apple","banana","cherry"} 
print("banana" in myset)

#Add set items 
myset = {"apple","banana","cherry"} 
myset.add("papaya")  
print(myset)    
 
myset = {"apple","banana","cherry"} 
tropical = {"pineapple","mango","papaya"}  
myset.update(tropical) 
print(myset)  

#Remove set items 
myset = {"apple","banana","cherry"} 
myset.remove("cherry") 
print(myset)   

myset = {"apple","banana","cherry"} 
myset.discard("cherry") 
print(myset)   

myset = {"apple","banana","cherry"} 
x = myset.pop()  
print(x)  
print(myset)  

myset = {"apple","banana","cherry"}  
myset.clear()
print(myset)

thisset= {"apple","banana","cherry"}  
del thisset 
#print(thisset)  

set1 = {"a","b","c","d",'a','b'}  
set2 = (1,2,3,4,4,3,2,1) 
set3  = set1.union(set2)
print(set3)  

set1 = {"a","b","c","d"}  
set2 = (1,2,3,4) 
set1.update(set2) 
print(set1)    

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) 
print(x)  

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y) 
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) 
print(x)  

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y) 
print(z)  

#isdisjoint() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y) 
print(z)  

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 
print(z)  

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y) 
print(z)  

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z)  

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z)

fd1 = [11,22,33,44,55,66,77]  
fd2 = [10,55,66,2+3j,56.6,33] 
fd3 = [11,22,3,44,66,77,99,10] 
print(list(set(fd1).union(set(fd2).union(set(fd3)))))  

print(list(set(fd1).intersection(set(fd2).intersection(set(fd3)))))  
print(list(set(fd1).difference(set(fd2).difference(set(fd3)))))

