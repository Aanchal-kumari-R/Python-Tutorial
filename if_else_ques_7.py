"""write a programm to check wheather the last digit of a number (enter by user) is divisible by 3 or not. """  

num = int(input("Enter a number:- "))  
last_num = num%10
if last_num%3 == 0: 
    print(last_num, 'is divisible by 3') 
else: 
    print(last_num,'is not divisible by 0')