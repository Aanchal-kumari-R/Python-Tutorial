df = () 
print(df) 

print(type(df))   

df1 =("aanchal",) 
print(type(df1)) 

df1 = ("aanchal") 
print(type(df1))

df1 = (23,45.78,["Ram","Shyam","Mohan"],3+5j) 
print(df1)   

print(df1[-1]) 
print(df1[-2])   
print(df1[-2][0])   
print(df1[:3])  
df1[-2].append(66) 
print(df1)  

df1[-2].pop() 
print(df1)   
 
#it's allow duplicate 
df1 = ("apple","banana","cherry","apple","guava","cherry")  
print(df1)  
print(len(df1))   

#tuple() Constructor 

thistuple = ((1,2,3,"Ram","Shyam","Kanha",3.54,3+2j))
print(thistuple)

if "Ram" in thistuple: 
    print("Yes , Ram is here")  

x = ("apple","banana","cherry")  
y = list(x) 
y[1] = "kiwi" 
x = tuple(y) 
print(x)  

#Add items 
x = ("apple","banana","cherry") 
y = list(x)  
y.append("Guava") 
x = tuple(y) 
print(x)
 
x = ("apple","banana","cherry") 
y = list(x) 
y.append(x) 
x = tuple(y) 
print(x)  

thistuple = ("apple","banana","cherry")  
y = ("Orange",)  
thistuple += y 
print(thistuple)  

#Remove 
thistuple = ("apple","banana","cherry")   
y = list(thistuple) 
y.remove("cherry")  
thistuple = tuple(y) 
print(thistuple)   

#Unpack Collection
thistuple = ("apple","banana","cherry")   
(red,green,yellow) = thistuple 
print(red) 
print(green) 
print(yellow)  

thistuple = ("apple","banana","cherry","Guava","papaya") 
(red,green,*yellow) = thistuple 
print(red) 
print(green) 
print(yellow) 

thistuple = ("apple","banana","cherry","Guava","papaya") 
(red,*green,yellow) = thistuple 
print(red) 
print(green) 
print(yellow)  

thistuple = ("apple","banana","cherry")   
for x in thistuple: 
    print(x)  

thistuple = ("apple","banana","cherry")   
for i in range(len(thistuple)) : 
    print(thistuple[i])


thistuple = ("Guava","apple","banana","cherry")   
i = 0 
while i<len(thistuple) : 
    print(thistuple[i]) 
    i = i+1

#Join tuple 
thistuple = ("Guava","apple","banana","cherry")   
tuple = ("apple","banana","cherry")   
tuple1 = thistuple+tuple 
print(tuple1)

thistuple = ("Guava","apple","banana","cherry")   
tuple = thistuple*2 
print(tuple) 
print(thistuple.index("Guava"))  
print(thistuple.count("Guava"))