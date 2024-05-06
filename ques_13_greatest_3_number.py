n1 = int(input("Enter the 1st number:- "))
n2 = int(input("Enter the 2nd number:- "))
n3 = int(input("Enter the 3rd number:- ")) 

if n1>n2: 
    if n1>n3:
        print(n1,"is a greater number.") 
    else:  
        print(n3,"is a greater number.") 
else: 
    if n2>n3: 
        print(n2,'is a greater number.') 
    else: 
        print(n3,"is the greater number.")


