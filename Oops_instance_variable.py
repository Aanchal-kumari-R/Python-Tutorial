#Example 1
class Employee: 
    def __init__(self): 
        self.name = "Aanchal Singh" 
        self.age = 23 
        self.account = 34234543434 
        self.sallary = 23000 
        self.loan = 45000 
    def show(self): 
        print(f"Name = {self.name} Age = {self.age} Account = {self.account} Sallary = {self.sallary} Loan = {self.loan}")  
df1 = Employee() 
df1.show()  

# Example 2
class Employee: 
    def __init__(self,n1,n2,n3,n4,n5): 
        self.name = n1 
        self.age = n2
        self.account = n3   #instance variable
        self.sallary = n4
        self.loan = n5
    def show(self): 
        print(f"Name = {self.name} Age = {self.age} Account = {self.account} Sallary = {self.sallary} Loan = {self.loan}")  
df1 = Employee("Aanchal Singh", 23,3434232323,23222,34300)  
print(df1.name)  
print(df1.account)
df1.show()  

df1.name = "Goldi" 
df1.age = 22 
df1.account = 4534234343 
df1.show()   

# Example 3 
class Students: 
    def __init__(self,nm,m): 
        self.name = nm 
        self.marks = m  
        print(f"Student = {self.name} Marks = {self.marks}" )
std1 = Students("Aanchal ",78) 
std2 = Students("Goldi ",89) 
std3 = Students("janki ",90) 


