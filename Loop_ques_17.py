"""Write a programm to add first nth terms of the following series using a for loop: 
1/1! + 2/2! + 3/3! .....n/n!""" 

num = int(input("Enter the number:- ")) 

sum = 0 
fact = 1 
i =1
while i<num:  
    fact = fact*i 
    sum = sum+i/fact 
    i = i+1 

print(round(sum,2))
