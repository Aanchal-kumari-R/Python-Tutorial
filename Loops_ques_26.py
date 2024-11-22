"""Write a program to display the numbers which are divisible by 13 but not by 3 between 100 and 500.(Exclusive both numbers)""" 

i = 101 
while i <= 500: 
    if i % 2 == 0: 
        print(i) 
    i = i+1 