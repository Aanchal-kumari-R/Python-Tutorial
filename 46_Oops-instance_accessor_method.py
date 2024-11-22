# Instance accessor/getter method:- This method is used to access or read the data of the variables. This method do not 
# modify the data in the variable. This is also called getter method.  
class mobile: 
    def __init__(self): 
        self.model = "Realme X" 
    def get_method(self): 
        return self.model 
realme = mobile() 
m = realme.get_method() 
print(m)