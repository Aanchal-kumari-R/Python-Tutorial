"""Accept the kilometers covered and calculate the bill according to the following criteria:-  
first 10 km       Rs.11/km 
second 90 km      Rs. 10/km   
After that        Rs. 9/km""" 

km = eval(input("Enter the covered kilometers :- "))
if km <=10: 
    bill = km*11 

elif km>10 and km<=100:  
    bill = 110+(km-10)*10 

elif km>100: 
    bill = 1010 +(km-90)*9 

print("Total payable amount is:- ",bill)