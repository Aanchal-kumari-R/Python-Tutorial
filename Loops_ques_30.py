"""Write a python program to find the sum of the following 
(accept values of x and n from user) 

1 + (x)2/2!..........x/n."""   

n = int(input("Enter the value of x:- ")) 
x = int(input("Enter the value of n :- ")) 

sum = 0 
i = 1 
while i<=n:  
    sum = sum + x**i/i 
    i+=1 
print(sum)
