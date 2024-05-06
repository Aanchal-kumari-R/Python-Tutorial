terms = int(input("Enter any number to identifity terms :- "))  
count = 0
n,m,j = 0,0,1  
if terms <= 0: 
    print("Number is invalid.") 
elif terms == 1: 
    print(n) 
elif terms == 2: 
    print(n) 
    print(m)  

else: 
    print("Tribonacci Sequence : ") 
    while count<terms:  
        print(n) 
        sum = n+m+j
        n = m 
        m = j 
        j = sum 
        count = count+1  

