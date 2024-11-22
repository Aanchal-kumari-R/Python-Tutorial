"""Write a python program to find the sum of the following 
(accept values of x and n from user) 

1 + x/1! + (x)2/2!..........x/n!."""   

n = int(input("Enter the value of n:- "))   
x = int(input("Enter the value of x:-")) 


sum = 1 
i = 1  
fact = 1
while i<n: 
    fact = fact * i  
    sum = sum + x**i/fact 
    i +=1 
print(sum)