df1 = range(10,21)
for i in df1: 
    print(i)  

print(list(range(10,21))) 

df2 = range(10,21) 
for n in df2: 
   print(n, end = " ") 
     
   

df3 =[11,22,33,44,55,66,77,88,99]
for i in df3:  
    if i%2 == 0:
      print(i) 
    
df1 = "DHYANANAD JHA" 
for i in df1: 
   print(i, end =" ") 

df3 =[11,22,33,44,55,66,77,88,99]
for i in df1: 
   print(df1.index(i),i) 

df1 = [11,22,33,44,55,66,77,88,11] 
for i in range(len(df1)): 
   print(i,df1[i])  

for i in range(10): 
   print(i)  

df1 = [11,22,33,44,55,66,77,88,11] 
for i in range(len(df1)): 
   if i%2 == 0: 
     print(i,df1[i])   

#enumerate()    
df1 = [11,22,33,44,55,66,77,88,11] 
for i,j in enumerate(df1): 
   print(i,j) 

#dictionary 
df1 = {1001:"Ram",1002:"Shyam",1003:"Mohan",1004:"Gita"} 
for i in df1: 
   print(i,df1[i])


for j,k in df1.items(): 
   print(j,k)     
#set  
df2 = {11,22,33,4,4,1,24,54,5} 
for i in df2: 
   print(i)  

#zip
df1 = [1,2,3,4,5,6,6,7] 
df2 =[11,22,33,44,55,66,77] 
df3 = [88,77,66,99,55,44,11] 
for i,j,k in zip(df1,df2,df3): 
   print(i,j,k) 

df1 = [1,2,3,4,5,6,6,7] 
df2 =[11,22,33,44,55,66,77] 
df3 = [88,77,66,99,55,44,11] 
for i,j,k in range(len(df1),len(df2),len(df3)): 
   print(i,j,k,df1[i],df2[j],df3[k])