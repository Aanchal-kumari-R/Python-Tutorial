


n1 = eval(input("Enter first number:- ")) 
n2 = eval(input("Enter second number:- ")) 


mess1 = input("Select Operations (+,-,*,//) :- ") 


if mess1 == '+': 
    print("Addition = ", n1+n2)  
elif mess1 == '-': 
    print("Subtraction = ", n1-n2)
elif mess1 == '*': 
    print("Multiplication = ", n1*n2) 

elif mess1 == '//': 
    print("Division = ", n1//n2)  

else: 
    print("Invalid Symbol")