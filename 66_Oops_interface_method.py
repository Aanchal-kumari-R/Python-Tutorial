# Interface :- In python, The interface concept is not explicitly available,like available in other language. Ex. in java.  
# In python ,an interface ia an abstract class, which contain only abstract method but not a single concrete method. 
# We connot create object object of an interface. we import abstractmethod from the abc module. we inherit ABC class in the class 
# for making interface which are imported from abc module.   

# USE:- We use interface when all the features need to be implemented diffrently for different object.


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


from abc import ABC , abstractmethod 

class father(ABC): 
    @abstractmethod 
    def disp(self): 
        pass 
     
    @abstractmethod
    def disp2(self):  
        pass 

class child(father):  
    def disp(self):
      print('child class')  

class grandchild(child): 
    def disp2(self):
        print('grandchild class') 

obj = grandchild() 
obj.disp() 
obj.disp2()
    
from abc import ABC , abstractmethod 

class father(ABC):  
    @abstractmethod
    def disp(self): 
        print("Main1")   

    @abstractmethod
    def disp2(self):  
        print("Main2") 

class son(father): 
    def disp(self): 
        super().disp() 
        print("Disp1") 

    def disp2(self): 
        super().disp2() 
        print("disp2")  

obj = son() 
obj.disp() 
obj.disp2()
