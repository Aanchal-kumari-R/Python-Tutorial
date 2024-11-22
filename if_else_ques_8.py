"""write a programm to accept the cost prize of a bike and display the road tax to be paid according to the following 
criteria :- 

Cost prize (in Rs.)              Tax 
>100000                           15% 
>50000 and <= 100000              10% 
<= 50000                          5% """ 
 
tax = 0
coast_prize = int(input("Enter the coast prize of a bike:- ")) 
if coast_prize>100000: 
    tax =   15/100 * coast_prize  
elif coast_prize >50000 and coast_prize<= 100000: 
    tax = 10/100 * coast_prize 
else: 
    tax =  5/100 * coast_prize 
print('tax to be paid:- ',tax)