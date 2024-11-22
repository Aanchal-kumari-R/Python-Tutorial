# 4):- Operator Overloading is a features in django that allows developers to redefine the behaviour of mathematical and comparison  
# operator for custom data types. 
# If any operator perform additional actions other than what it is meant for, it is called operator overloading.

class ramayan: 
    def __init__(self): 
        self.page = 4500
    
    def __add__(self,other): 
        return self.page + other.page
class mahabharat: 
    def __init__(self): 
        self.page = 67000 

r1 = ramayan() 
m1 = mahabharat() 

print(r1+m1)