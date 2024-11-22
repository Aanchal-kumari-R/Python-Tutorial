"""Write a programm to convert Decimal to Binary. """ 
num = int(input("Enter a positive number:- "))    #12
bin = 0 
p = 1 
n = num  
while n>0 :
    rem = int(n%2) 
    bin = bin + rem * p 
    p = p*10 
    n = n/2 
print("Binary number of ",num ,"is :- ",bin)


