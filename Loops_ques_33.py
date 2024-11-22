"""Write a programm to find the sum of following series:-  
 1 + 4 - 9 + 16 - 25 + 36..........n terms""" 

n = int(input("Enter the terms:- "))  

sump = 1 
sumn = 0 
i = 2
while i<=n: 
    if i%2 == 0 : 
        sump = sump + i**2 
        i+=1 
    else: 
        sumn = sumn + i**2 
        i+=1 

print(sump-sumn)