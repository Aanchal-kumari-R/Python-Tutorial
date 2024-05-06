#Lambda Function
calc = lambda n1,n2 : n1+n2 
print(calc(43,45))  

calc = lambda *n1: sum(n1) 
print(calc(12,65,45,98)) 

even_check = lambda n1: 'n is even number' if n1%2==0 else 'n is odd number' 
print(even_check(12)) 

even_check = lambda n1: n1%2==0
print(even_check(12)) 

#filter 

df1 = [22,21,343,54,23,64,65] 
calc = filter(lambda n: n%2!=0, df1) 
print(list(calc)) 

df2 = ["Mohan","Shyam","Ram","Meenu","Reenu","Rita"] 
df = list(filter(lambda n: n.count('a')>0,df2)) 
print(df)  

#Map 
df = [11,22,33,44,55,66,77,88] 
df =  list(map(lambda n1:n1**2,df1)) 
print(df)  

df2 = ["Mohan","Shyam","Ram"] 
df = map(lambda n1:"Mr " +n1+" Prasad",df2) 
print(list(df))  

#Reduce 
from functools import reduce  
df5 = [10,20,30,40,50]  
df = reduce(lambda x,y: x+y,df5) 
print(df)   

#Recursive Function 
def recursive_fibonacci(n): 
    if n<=1: 
        return n  
    else: 
        return(recursive_fibonacci(n-1)+recursive_fibonacci(n-2)) 
n_terms = 10 

if n_terms <= 0: 
    print("Invalid Number ! Please input positive value") 
else: 
    print("fibonacci series:") 
for i in range(n_terms) : 
    print(recursive_fibonacci(i))
