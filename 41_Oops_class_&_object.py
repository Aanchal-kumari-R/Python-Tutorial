# Class :- Class is a collection of objects. Class is a blueprint and prototype from which the objects are being created. 
# It is a logical entity that contains some attributes and methods.  

# Object :- Object is an entity that has a state and behavior associated with it. It may be any real-world object such as  
# chair, pen, table etc.  


class calc() : 
    def add(self): 
        n1 = 10 
        n2 = 20 
        print("Addition = ", n1+n2) 
    def sub(self): 
        n1 = 30 
        n2 = 20 
        print("Subtraction =", n1-n2) 
df1 = calc() 
df1.add()  
calc.add(df1)
df1.sub()   
calc.sub(df1)

 
class calc() : 
    def add(n):  
        n1 = eval(input("Enter first number:- ")) 
        n2 = eval(input("Enter second nubmer:- "))
        print("Addition = ", n1+n2) 
    def sub(n):  
        n1 = eval(input("Enter first number:- ")) 
        n2 = eval(input("Enter second nubmer:- "))
        print("Subtraction =", n1-n2) 
df1 = calc() 
df1.add() 
df1.sub()  

