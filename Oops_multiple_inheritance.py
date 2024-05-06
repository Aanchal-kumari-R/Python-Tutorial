class parent: 
    def __init__(self): 
        self.name1 = "Vijay Singh" 
        self.sallary1 = 20000 
        self.loan1 = 200000 
        self.account1 = 789989890900 
        super().__init__() 
    def get_show(self): 
        print(f"Name = {self.name1}, Sallary = {self.sallary1}, Loan = {self.loan1}, Account = {self.account1}")  
        super().get_show() 

class mother: 
    def __init__(self): 
        self.name2 = "Usha Singh" 
        self.sallary2 = 2000 
        self.loan2 = 20000
        self.account2 = 898099890900 
    def get_show(self): 
        print(f"Name = {self.name2}, Sallary = {self.sallary2}, Loan = {self.loan2}, Account = {self.account2}")  

class child(parent,mother): 
    def __init__(self): 
        self.name = "Aanchal Singh" 
        self.sallary = 40000 
        self.loan = 400000 
        self.account = 43534589890900  
        super().__init__()   
    def get_show(self): 
        super().get_show() 
        print(f"Name = {self.name}, Sallary = {self.sallary}, Loan = {self.loan}, Account = {self.account}") 
    def total_property(self): 
        print(f"Total property of child  = {self.sallary+self.sallary1+self.sallary2}, and total Loan = {self.loan+self.loan1+self.loan2}.")  
obj = child() 
obj.get_show()  
obj.total_property()
print(obj.name) 
print(obj.name1) 
print(obj.name2)

