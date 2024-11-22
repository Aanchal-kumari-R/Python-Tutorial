# Instance Method :- Instance method are the methods which act upon the instance variable of the class. 
# Instance method need to know the memory address of the instance which is provided through self variable  
# by default as first parameter for the instance method.  
# There are two types of instance method:- 
# 1) Accessor Method 
# 2) Mutator Method 
class mobile: 
    def __init__(self): 
        self.model = "Realme X" 
    def show_model(self,p): 
        self.price = p 
        print(f"Model = {self.model} , Price = {self.price}") 
realme = mobile() 
       
realme.show_model(10000)