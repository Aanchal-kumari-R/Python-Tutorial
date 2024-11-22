''' 
Multilevel Inheritance:- In multilevel inheritance , feature of the base class ans the derived class are further inherited into 
new derived class. This is similar to a relationship representing a child and a grandfather. 


'''
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

class father: 
    def __init__(self): 
        print("Father constructor") 

    def show(self): 
        print("Father Method") 

class son(father): 
    def __init__(self):  
        super().__init__()
        print("Mother constructor") 

    def show(self): 
        print("Mother Method")  

class grandson(son): 
    def __init__(self): 
        super().__init__()
        print("Grandson constructor") 

    def show(self): 
        print('GrandSon Method') 

g = grandson()



