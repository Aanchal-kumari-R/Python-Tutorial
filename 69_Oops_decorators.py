# * Python decorator are a powerful and versatile tool that allow us to modify the behaviour 
# of the function and method. They are a way to extend the functionality of a function or  
# method without modify the same code.  
 
# * A decorator is a function that take another functions as an argument and returns a new  
# functions that behaviour of the original function.

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
    print("....Executing all steps of Transaction....") 
hello()