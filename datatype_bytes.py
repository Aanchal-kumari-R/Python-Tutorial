#memory efficiency
import sys 

data1 = [10,20,30,40]
data2 =bytes([10,20,30,40]) 
print(max(data2))  
print("Memory consumed by data1 :",sys.getsizeof(data1)) 
print("Memory consumed by data2 :",sys.getsizeof(data2))

df = bytes([11,2,233,45,67])  
print(df)  
 
df1 = bytes([11,2,233,54,67])  
print(type(df1))  

print(df[0])  
print(df[0:3])
print(df[:3])  
print(df[3:])  

print(len(df)) 

print(bytes([8])) 
print(bytes(8))