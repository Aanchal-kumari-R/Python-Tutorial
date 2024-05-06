class grandfather: 
    def __init__(self,grandfathername): 
        self.grandfathername = grandfathername 


class father(grandfather): 
    def __init__(self,fathername, grandfathername): 
        self.fathername = fathername 
        grandfather.__init__(self,grandfathername) 


class son(father):  
    def __init__(self,sonname,fathername,grandfathername): 
        self.sonname = sonname 
        father.__init__(self,fathername,grandfathername) 
    def print_name(self): 
        print("Grandfather name = ", self.grandfathername)
        print("Father name = ", self.fathername)
        print("Son name = ", self.sonname)  

obj = son("Sonu","Shyamlal","Ramlal") 
obj.print_name()

