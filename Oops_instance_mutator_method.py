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