digit = eval(input("Enter any numer to print the sum of digit :- "))  
sum = 0
while digit>0: 
    r = digit%10  
    sum = sum+r 
    digit = digit//10 
print("The sum of digit is ", sum)