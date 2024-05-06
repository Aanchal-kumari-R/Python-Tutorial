i = 0 
while i<=10: 
    print(i,"Python class") 
    print("This is while loop") 
    i+=1 
print("This is out of while loop")  


print("Table of 10 is:")
n = 10 
while n<=100: 
    print(n) 
    n+=10   

print("Table of 13 is:")
t = 13 
while t<=131: 
    print(t)  
    t+=13 

c = 20 
while c>=10: 
    print(c) 
    c-=1 

num  = eval(input("Dear user,Enter any number to write a table:")) 
t = 1  
while t<=10: 
    print(num,"*",t,"=",num*t)  
    t+=1 

num  = eval(input("Dear user,Enter any number to write a table:")) 
t = 1  
while t<=10: 
    print(f"{num}*{i}={n*i}")  
    t+=1 


num  = eval(input("Dear user,Enter any number to write a table:")) 
m = 1 
while m<=10: 
    print(m*num,end =" ") 
    m+=1  
print("This is out while loop")

num  = eval(input("Dear user,Enter any number to write a table:")) 
m = 1 
while m<=10: 
    print(m*num,end ="\t") 
    m+=1