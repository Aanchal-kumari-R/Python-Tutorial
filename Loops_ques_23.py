"""Write a programm to accept 10 numbers from the user and display it's average."""  

sum = 0
i = 0 
while i < 10: 
   nums = int(input("Enter the numbers:- "))    
   sum =  sum+nums  
   i = i+1 
avg = sum/10
print("The average is :- ",avg)

