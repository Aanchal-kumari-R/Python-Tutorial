# write a programm to find the sum of the digits of a number accepted from the user.

n1 = int(input("Enter the digits:- ")) 

sum = 0 
r1 = 0  
while n1 != 0: 
    r1 = n1%10 
    sum = sum+r1   
    n1 = n1//10 

print(sum) 