"""Write a programm to display the sum of odd numbers and even numbers separately that fall between two numbers accepted from 
 the user.(including both numbers) using while loop.""" 

num1 = int(input("Enter the first number:- ")) 
num2 = int(input("Enter the seconf number:- ")) 
sume = 0 
sumo = 0
if num1>num2: 
    while num2 <= num1: 
        if  num2 % 2 == 0: 
            sume = sume + num2 
            num2 = num2 +1 
        else:  
            sumo = sumo + num2 
            num2 = num2 + 1  

else: 
    while num1 <= num2 : 
        if num1 % 2 == 0: 
            sume = sume + num1 
            num1 = num1 + 1 
        else: 
            sumo = sumo + num1 
            num1 = num1 + 1 

print("The sum of even number is :- ",sume) 
print("The sum of odd number is ",sumo)


