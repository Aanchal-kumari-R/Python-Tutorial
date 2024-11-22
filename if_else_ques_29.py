"""Accept the number of days from the user and calculate the charge for library according to following:- 
Till  five days          Rs. 2/day. 
Six to 10 days           Rs. 3/day.     
11 to 15 days            Rs. 4/day. 
After 15 days            Rs. 5/day. """   


days = int(input("Enter the number of days:- ")) 

if days<=5: 
    amt = days*2 

elif  days>= 6 and days<=10: 
    amt = days*3 

elif days>10 and days<=15: 
    amt = days*4 

else: 
    days>15 
    amt = days*5 
print("Amount is:- ",amt)


