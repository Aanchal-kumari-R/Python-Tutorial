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