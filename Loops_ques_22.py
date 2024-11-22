"""Write a python programm to sum the swquence. 
1 + 1/1!  +1/2! + 1/3!........1+n/!""" 

num = int(input("Enter a number:- ")) 
fact = 1 
sum = 1 
i = 1 
while i<=num: 
    fact = fact * i  
    sum = sum + 1/fact 
    i+=1 
print("Sum of sequence is:- ",sum) 
