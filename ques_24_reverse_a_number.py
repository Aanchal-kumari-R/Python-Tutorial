number = int(input("Enter any to reverse :- ")) 

while number>0: 
    r = number%10 
    print(r , end = "") 
    number = number//10 