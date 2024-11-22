# Hybrid inheritance:- Hybrid inheritance is a combination of single,multiple and hierarchical inheritance in OOPs. It is a type 
# of inheritance in which multiple inheritance is used to inherit the properties of multiple base class into a  single derived 
# class and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

class A: 
    def func(self): 
        print("Hello from class A.") 

class B(A): 
    def func1(self): 
        print("Hello from class B.") 

class C(A): 
    def func2(self): 
        print("Hello from class C.") 

class D(B,C): 
    def func3(self): 
        print("Hello from class D.") 

obj = D() 
obj.func() 
obj.func1() 
obj.func2() 
obj.func3() 

class grandfather: 
    def __init__(self):  
        print("Grandgather's constructor") 

    def show(self): 
        print("grandfather's method") 

class father(grandfather):   
    def __init__(self):  
        super().__init__()
        print("father's constructor") 

    def show(self): 
        super().show() 
        print("father's method")  

class mother(grandfather):  
    def __init__(self):  
        super().__init__()
        print("mother's constructor") 

    def show(self): 
        super().show() 
        print("mother's method")    


class child(father,mother): 
    def __init__(self): 
        super().__init__()
        print("child's constructor") 

    def show(self):  
        super().show()
        print("child's method") 

c = child() 
c.show()

# f = father()  
# f.show()


# m = mother()  
# m.show()






    