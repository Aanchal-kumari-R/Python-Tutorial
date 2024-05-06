from abc import ABC , abstractmethod 

class Father(ABC): 
    @abstractmethod 
    def disp(self): 
        pass 

class Child(Father): 
    def disp(self): 
        print("Child class.") 
        print("Defining abstract method.") 

child = Child() 
child.disp()