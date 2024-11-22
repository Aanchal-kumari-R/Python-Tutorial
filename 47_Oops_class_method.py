# Class Method :- Class methods are the methods which act upon the class variables or static variables of the class. Decorator @classmethod need  
# to write above the class method. By default the first parameter pf the class cls which refers to the class itself. 

class mobile:  
    fp = 'yes' 
    @classmethod 
    def show_model(cls,r): 
        cls.ram = r 
        print("FingerPrint :", cls.fp) 
        print("RAM :", cls.ram) 
realme = mobile() 
mobile.show_model("4GB")