"""A company decided to give bonus to employee according to following criteria:-  

Time period of service          Bonus  
More than 10 years              10% 
>= 6 and <= 10 years             8% 
less than 6 years                6%    

Ask user for their sallary and years of service and print the net bonus amount. """ 

bonus = 0
experience = int(input("Enter the years of service:- ")) 
sallary = eval(input("Enter the sallary of the employee:- ")) 

if experience>10: 
    bonus  = 10/100*sallary  

elif experience<=10 and experience>=6: 
    bonus = 8/100*sallary  

elif experience<6: 
    bonus = 5/100*sallary 

print("The bonus of employee is",bonus)