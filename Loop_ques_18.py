"""Write a programm to enter the numbers till the user wants and at the end it  
should display the sum of all the numbers entered. """ 


ch = 'Y' 
sum = 0  
while ch.upper() == 'Y' or ch == 'y':
   num = int(input('Enter any number:- '))  
   sum = sum + num 
   ch = input("Do you want to continue(Y,N):- ")  
print('Sum of all numbers is:- ',sum)

