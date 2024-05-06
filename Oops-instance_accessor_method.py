class mobile: 
    def __init__(self): 
        self.model = "Realme X" 
    def get_method(self): 
        return self.model 
realme = mobile() 
m = realme.get_method() 
print(m)