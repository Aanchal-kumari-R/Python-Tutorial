""" Abstraction:- Abstraction is a process of hiding the implementation details fron the users only the highlighted set of 
services provided to the user. 
Abstraction is one of the most essential concepts of python OOPs. """

""" Abstract Class:- A class which derived from abc class which belongs to abc module is known as abstract class in python. 
Abc class is known as meta class which means a class that defines the behaviour of other classes.  
Abstract class can have both abstract method and concrete method. 
Abstract class need to be extended and its method implemented.  
PVM can not create objects of an abstract class. """ 

""" Abstract Method:- A abstract method is a method whose action is redefined in the child classes as per the 
 requierment of the object. We can declare a method as abstract method by using @abstractmethod decorator.   
""" 

""" Concrete Method:- A concrete method is a method whose action is defined in the abstract class itself.""" 

""" Use :- We use abstract class when there are some common feature shared by all the objects as they are."""

from abc import ABC , abstractmethod 

class Father(ABC):  
    @abstractmethod
    def disp(self): # declare the abstract method
        pass  

    def show(self): # Concrete method 
        print("concrete method") 

class child(Father): #CHILD CLASS
    def disp(self): #Defining abstract method 
        print("Child class") 
        print("Defining abstract method.") 

c = child() 
c.disp() 
c.show() 
        

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()