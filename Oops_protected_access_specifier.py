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
