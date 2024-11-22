"""Accept the market price from the user and calculate the Net amount as(Marked Price - Discount) to pay according to  
following criteria:-  
Marked price                       Discount 
>10000                            20% 
>7000 and <= 10000                15% 
<= 7000                           10%"""     

per = 0
mp = int(input("Enter the market price:- ")) 
if mp > 10000: 
    per = 20/100*mp 
    disc = (mp-per) 
elif mp>7000 and mp<=10000: 
    per = 15/100*mp 
    disc = (mp-per) 

elif mp<=7000: 
    per = 10/100 *mp  
    
disc = (mp-per) 
print("Net amount is:- ", disc)
    