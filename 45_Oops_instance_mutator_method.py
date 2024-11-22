# Instance mutator/setter method:- This method is used to access or read and modify the data of the variable.This method is used 
# to modify the data in the variable. This is also called setter method.
class mobile: 
    def __init__(self): 
        self.model = "Realme X" 
    def set_model(self): 
        self.model = "Realme 2" 
realme = mobile() 
# Before setting 
print(realme.model) 
# After setting 
realme.set_model() 
print(realme.model)