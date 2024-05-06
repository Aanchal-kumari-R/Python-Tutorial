num = int(input("Enter any number to check number is perfect or not :- ")) 
sum = 0  


for i in range(1,num): 
    if num % i == 0: 
        sum = sum+i  
if(num == sum): 
    print("This is perfect number.") 
else : 
    print("This is not perfect number.") 
        