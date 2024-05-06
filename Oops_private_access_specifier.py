class Geek: 
    __name = None  
    __roll = None 
    __branch = None 

    def __init__(self,name,roll,branch): 
        self.__name = name 
        self.__roll = roll 
        self.__branch = branch 

    def __privateFunction(self): 
        print("Name :",self.__name) 
        print("Roll ",self.__roll) 
        print("Branch :",self.__branch) 

    def accessprivateFunction(self): 
        self.__privateFunction() 


obj = Geek("Aanchal Singh",12,"Information Technology") 
obj.accessprivateFunction()