class employee:  
    cmp = "TCS"  #class/static variable
    def __init__(self): 
        self.name = "Aanchal Singh" 
        self.age = 23 
        self.account = 87889989809 
        self.sallary = 34000 
        self.loan = 88989 
    def show(self): 
        print(f" Company = {employee.cmp} ,  Name = {self.name} , Age = {self.age} , Account = {self.account} , Sallary = {self.sallary} , Loan = {self.loan}") 
df1 = employee() 
df1.show()  

employee.cmp = "TaTa Motors" #modify through class
df1.show() # we can not change class name through object  

df2 = employee()   


  

  