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