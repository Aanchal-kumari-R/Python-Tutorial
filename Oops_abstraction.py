from abc import ABC , abstractmethod 

class Father(ABC):  
    @abstractmethod
    def disp(self): 
        pass  

    def show(self): 
        print("concrete method") 

class child(Father): 
    def disp(self):
        print("Child class") 
        print("Defining abstract method.") 

c = child() 
c.disp() 
c.show() 
        

