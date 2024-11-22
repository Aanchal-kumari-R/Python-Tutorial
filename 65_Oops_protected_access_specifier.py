''' Protected Access Modifier:- In Object Oriented Programming (OOP). The term 'Protected' is used to describe a member   
(i.e. method or attribute) of a class that is intended to be accessed only by the class itself and its subclass. In python, the 
convention for indicating that a member is protected is to prefix its name with a single underscore(_). '''
class Students: 
    _name = None 
    _roll = None
    _branch = None 
    def __init__(self,name,roll,branch): 
        self._name = name 
        self._roll = roll 
        self._branch = branch  

    def _protectedFunction(self): 
        print('Roll :',self._roll) 
        print("Branch :",self._branch) 

class Geek(Students): 
    def __init__(self,name,roll,branch): 
        Students.__init__(self,name,roll,branch) 

    def accessProtectec_Function(self): 
        print("Name :",self._name) 

        self._protectedFunction() 

obj = Geek("Aanchal Singh", "231232","Information Technology") 
obj.accessProtectec_Function()   



class student: 
    def __init__(self): 
        self._name = "Aanchal" 

    def _funName(self): 
        return "Aanchal Singh" 

class subject(student): 
    pass 

obj = student() 
print(obj._name) 
print(obj._funName()) 

obj1 = subject() 
print(obj1._name) 
print(obj1._funName()) 


