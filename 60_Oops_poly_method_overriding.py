# 3):- Method Overriding:- Whenever we writtin method name with same signature in parent and child class 
# that is called method overriding.
class call: 
    def show(self): 
        print("This is a parent class") 

class receive(call):
    def show(self):  
        super().show() 
        print("This is a child class.")

df = receive() 
df.show()   

class arithmetic: 
    def calc(self,a,b): 
        print("Addition = ",a+b) 

class math(arithmetic): 
    def calc(self,a,b):  
       super().calc(10,20)
       print('multiplication = ',a*b)  
    # pass
    
df = math() 
df.calc(10,20)