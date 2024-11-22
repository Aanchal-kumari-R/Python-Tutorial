"""Accept the electric units from user and calculate the bill according to the following criteria:-  
First 100 units          free 
Second 200 units         Rs. 2 per day 
Third 300 units          Rs. 5 per day """ 

amt = 0
units = eval(input("Enter the electrics units:- ")) 

if units <= 100: 
    amt = 0 

elif units>100 and units<=300:  
    amt = (units-100) *2 

else:  
    amt = 400+ (units-300)*5 

print("Bill is :-", amt) 

