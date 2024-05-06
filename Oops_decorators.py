def decorator(func): 
    def wrapper(): 
        print("Transaction Initiated")  
        func() 
        print("Transaction Completed") 
    return wrapper 
def hello(): 
    print("....Executing all steps of Transaction...") 
hello1 = decorator(hello) 
hello1()  



def decorator(func): 
    def wrapper(): 
        print("Transaction Initiated.") 
        func() 
        print("Transaction completed.") 
    return wrapper 
@decorator 
def hello(): 
    print("....Exxecuting all steps of Transaction....") 
hello()