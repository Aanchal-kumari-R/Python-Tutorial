""" Write a programm to enter the numbers till the user enter zero and at the end it should display the count of 
positive and negative numbers entered. """ 

count = 0 
count1 = 0  
num = 1
while num != 0: 
    num = int(input("Enter any numbers:- ")) 
    if num >= 0 :  
        count = count + num 
    elif num <= 0 : 
        count1 = count1 +num  
print("The positive number is:- ",count) 
print("The negative number is:- ",count1)

