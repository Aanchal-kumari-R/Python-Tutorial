"""Write a programm to print all the factors of a number using for loop.""" 

num = int(input("Enter any number:- ")) 

i = 1 
while i <= num: 
    if num % i == 0: 
        print(i) 
    i+=1 