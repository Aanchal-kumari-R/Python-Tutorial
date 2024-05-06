df = range(12,3,45) 
print(df) 

print(type(df))   

df = range(10,30,1)
print(list(df)) 

df = range(10,30,2)
print(list(df)) 

df = range(10,30,3)
print(list(df))  

df = range(50,10,-1) 
print(list(df))  

df = range(50,10,-2) 
print(list(df))   
print(df[0]) 
print(df[-1]) 
print(len(df))  
print(max(df)) 
print(min(df))  

df = [12,5,8,16,45,67,11,6,9]  
df.sort()
print(df)  
print(df[::-1])