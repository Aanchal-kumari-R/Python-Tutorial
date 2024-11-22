""" write a programm to calculate the electricity bill(accept number of units from the users) according to the following criteria:- 
units                                    price 
first 100 units                          no charge 
next 100 units                            Rs 5 per units 
after 200 units                           Rs 100 per units""" 

amount = 0 
units = int(input("Enter units of electricity bills:- ")) 

if units<=100:  
    amount = 0 
    
if units>100 and units<=200: 
    amount = (units-100)*5  

if units>200: 
    amount = 500+(units-100)*10 
print("Total payable amount is",amount) 


