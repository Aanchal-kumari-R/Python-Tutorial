# write a programm to find the sum of the digits of a number accepted from the user.

nm = int(input('Enter the digits:- ')) 

rm = 0 
prdt = 1 

while nm != 0: 
    rm = nm%10 
    prdt = prdt*rm 
    nm = nm//10 

print(prdt)