class calc: 
    def add(self): 
        n1 = 10 
        n2 = 20 
        print("Addition = ",n1+n2) 
    def sub(self): 
        n1 = 30 
        n2 = 20 
        print("Subtraction = ",n1-n2)  
class arth(calc): 
    def Mult(self): 
        n1 = 50 
        n2 = 10 
        print("Multiplication = ", n1*n2) 
    def Div(self): 
        n1 = 10 
        n2 = 30 
        print("Division = ",n1/n2) 
obj = arth() 
obj.add() 
obj.sub() 
obj.Mult() 
obj.Div()