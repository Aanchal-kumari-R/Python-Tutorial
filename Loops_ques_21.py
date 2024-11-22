"""Write a programm to convert binary to decimal number:- """ 

bin = input("Enter a binaty number:- ")  
dec = 0 
p = 0 
for i in reversed(bin): 
    dec = dec + int(i) * pow(2,p) 
    p = p+1 
print("Binary number of",bin,'is:- ',dec)
