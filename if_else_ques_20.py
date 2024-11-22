# Accept the age of 4 people and display oldest one?  

p1 = int(input("Enter the age of p1:- "))
p2 = int(input("Enter the age of p2:- "))
p3 = int(input("Enter the age of p3:- "))
p4 = int(input("Enter the age of p4:- "))  

if p1>p2 and p1>p3 and p1>p4: 
    print('p1 is the oldest person.') 

elif p2>p1 and p2>p3 and p2>p4: 
    print('p2 is the oldest person.') 

elif p3>p1 and p3>p2 and p3>p4: 
    print('p3 is the oldest person.') 

elif p4>p1  and p4>p2  and p4>p3: 
    print('p4 is the oldest person.')