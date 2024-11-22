# write a programm to reverse the number accepted from  user using while loop.  

num = int(input("Enter the number for reverse:- ")) 

rem = 0
rev = 0 

while num != 0: 
    rem = num % 10 
    rev = rev*10 + rem 
    num = num//10 

print("Reverse number is :- ",rev)