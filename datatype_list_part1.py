df=[] 
print(df)  

print(type(df))   
df = [12,34.5,3j+5,"Mohan","Sohan"]  
print(df)  

print(df[0])  
print(df[-1])   

print(df[:3])  
print(df[::-1]) 

df[0] = 899 
print(df)   

print(len(df))    

#list constructor()  
thislist = list(["apple","banana",45,45.9,"cherry"]) 
print(thislist)  
print(thislist[2:5])   
print(thislist[-4:-1])

#check the items in list 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: 
    print("yes,'apple' is in the fruits list")  
 
#change list items 
thislist = ["apple","banana","cherry"]  
thislist[1] = "blackcurrant" 
print(thislist)  
 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] =["blackcurrant","watermelon"]  
print(thislist)   

thislist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] 
print(thislist)  

#insert list items  
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon") 
print(thislist)  
 
#insert list in list
thislist = ["apple","banana","cherry"]  
tropical = ["mango","pineapple","papaya"] 
thislist.extend(tropical) 
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thistuple = ["kiwi","orange"]  
thislist.extend(tropical) 
print(thislist) 

#Remove list items 
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple") 
print(thislist)  
 
thislist = ["apple", "banana", "cherry","banaba","kiwi"]  
thislist.remove("banana")  
print(thislist)  

#pop 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) 
print(thislist)

thislist = ["apple", "banana", "cherry"] 
thislist.pop()
print(thislist)  

thislist = ["apple", "banana", "cherry"]
del thislist[0] 
print(thislist)  

#Clear the list  
thislist = ["apple", "banana", "cherry"]
thislist.clear() 
print(thislist)  

#Loops through a list 
thislist = ["apple", "banana", "cherry"]
for x in thislist: 
    print(x)  

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):  
   print(thislist[i]) 

thislist = ["apple", "banana", "cherry"]
i = 0 
while i<len(thislist): 
    print(thislist[i]) 
    i=i+1  

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]   

