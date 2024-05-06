class mobile: 
    def __init__(self): 
        self.model = "Realme X" 
    def show_model(self,p): 
        self.price = p 
        print(f"Model = {self.model} , Price = {self.price}") 
realme = mobile() 
       
realme.show_model(10000)