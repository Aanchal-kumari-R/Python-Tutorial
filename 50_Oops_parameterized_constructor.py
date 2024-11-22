# Parameterized Constructor:- When the constructor accepts argument along with self , it is known as parameterized constructor. 
# These argument can be used inside the class to assign the values to the data members.
class deltails: 
    def __init__(self,animal,group): 
        self.animal = animal 
        self.group = group  
obj = deltails("Crab","Crustances") 
print(obj.animal,'belongs to the',obj.group ,"group.") 
 
 