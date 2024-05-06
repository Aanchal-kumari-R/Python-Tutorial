#Write a program in which user input a number and check the number is even or not 
number = eval(input("Enter any number:")) 
if number%2==0: 
    print("Even number") 
else: 
    print("Odd number")  


num = eval(input("Enter any number :")) 
if num>0: 
    if num%2==0: 
        print(num,"is Positive even number") 
    else: 
        print(num,"is Positive odd number") 
else: 
    if num%2==0: 
        print(num,"is Negative even number") 
    else: 
        print(num,"is Negative odd number")