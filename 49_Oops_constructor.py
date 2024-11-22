# * Constructor :- A constructor is a special method in a class used to create and initialized an object of a class. Constructor is 
# involved automatically , when an object of a class is created.  
# * __init__ is one of the reserved function in python. In object oriented programming , it is known as a constructor. We can also 
# create constructor by defining the function name with same class name.

class person: 
    def __init__(self,name,occ): 
        self.name = name 
        self.occ = occ 
    def info(self): 
        print(f"{self.name} is a {self.occ}") 
a = person("Aanchal","Developer")   
b = person("Divya", "Developer")
a.info() 
b.info()
        
