''' Inheritance :- Inheritance is a mechanism that allow us to create a hierarchy of classes that share a 
set of properties and method by deriving a class from another class. Inheritance is the capability of  
one class to derive or inherit the properties from another class '''

''' ADVANTAGES:-   
1):- Code Reusability:- The child class copies all the attributes and methods of the parent class into  
 its class and use. 
 2):- Less Development and Maintenance Costs:- Changes must be made in the base class and all derived  
 classes will automatically follow.''' 

''' DISADVANTAGES :-  
1):- Decrease the Execution Speed:- Loading multiple classes they are independent. 
2):- Tightly Coupled Classes:- Even thought parent classes can be executed independently. Child class  
can only be conducted by defining their parent classes.'''

''''TYPES OF INHERITANCE:- There are five types of inheritance in python. 
1):- Single Inheritance 
2):- Multiple ''  
3):- Multilevel '' 
4):- Hierarchical '' 
5):- Hybrid        '' 

1:- Single Inheritance:- 
A class that is derived from only one class is called singhle inheritance. 
Ex:- '''

class calc: 
    def add(self): 
        n1 = 10 
        n2 = 20 
        print("Addition = ",n1+n2) 
    def sub(self): 
        n1 = 30 
        n2 = 20 
        print("Subtraction = ",n1-n2)  
class arth(calc): 
    def Mult(self):  
        n1 = 50 
        n2 = 10 
        print("Multiplication = ", n1*n2) 
    def Div(self): 
        n1 = 10 
        n2 = 30 
        print("Division = ",n1/n2) 
obj = arth() 
obj.add() 
obj.sub() 
obj.Mult() 
obj.Div()  



class parent: 
    def __init__(self): 
        self.name1 = 'vijay singh' 
        self.sallary1 = 125700 
        self.account1 = 4389423832 
        self.loan1 = 3423000 

    def show(self): 
        print(f"\nName ={self.name1}\nSallary = {self.sallary1}\nAccount = {self.account1}\nLoan = {self.loan1}\n")  

class child(parent):  
    def __init__(self): 
        self.name = 'Aanchal Singh' 
        self.sallary = 125700 
        self.account = 4389423832 
        self.loan = 3423000   
        super().__init__()

    def show(self):  
        super().show()
        print(f"Name = {self.name}\nSallary = {self.sallary}\nAccount = {self.account}\nLoan = {self.loan}") 

c = child() 
# print(c.account1) 

c.show()
