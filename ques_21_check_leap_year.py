year = int(input("Enter any year to check leap year or not :- ")) 

if year%100 == 0 and year%400 == 0 or year%100!= 0 and year%4 == 0: 
    print(year ," is the leap year.") 
    
else: 
    print(year," is not leap year.")