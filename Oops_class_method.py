class mobile:  
    fp = 'yes' 
    @classmethod 
    def show_model(cls,r): 
        cls.ram = r 
        print("FingerPrint :", cls.fp) 
        print("RAM :", cls.ram) 
realme = mobile() 
mobile.show_model("4GB")