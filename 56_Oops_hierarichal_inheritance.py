# Hirarchical Inheritance :- When more than one derived class are created from a single base class this type of inheritance 
# is called hierarchical inheritance.

class parent: 
    def func(self): 
        print("This is a parent class.") 
class child1(parent): 
    def func1(self): 
        print("this is child 1 class.") 
class child2(parent): 
    def func2(parent): 
        print("this is child 2 class.") 
class child3(parent): 
    def func3(parent): 
        print("this is child 3 class.") 
obj1 = child1()
obj2 = child2()
obj3 = child3() 
obj1.func()
obj1.func1()
obj2.func()
obj2.func2()
obj3.func()
obj3.func3()  

class father: 
    def __init__(self): 
        print("father's Constructor") 

    def show(self): 
        print("father's Method ") 

class son(father): 
    def __init__(self): 
        super().__init__()
        print("son's constructor") 

    def show(self):  
        super().show()
        print("son's Method") 

class daughter(father): 
    def __init__(self):  
        super().__init__()
        print("daughter's constructor") 
    
    def show(self):  
        super().show()
        print("Daughter Method") 

s = son() 
s.show() 

d = daughter() 
d.show()