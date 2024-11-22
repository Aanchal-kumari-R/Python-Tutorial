# Instance variable made for particular instance. In instance variable , seprate copy is created for every object. 
# Value of variables differs from object to object. Modification in one object won't effect other objects.

# Self Keyword:- Python must have an extra first parameter in the method definition. We do not give a value for this 
# parameter. When we call the method , python provide it. The reason we need to use self is because python do not use  
# '@' syntax to refer to instanve variable. 
 
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
    def __init__(self,n1,n2,n3,n4,n5): #constructor
        self.name = n1 
        self.age = n2
        self.account = n3   #instance variable
        self.sallary = n4
        self.loan = n5
    def show(self): #instance method
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


