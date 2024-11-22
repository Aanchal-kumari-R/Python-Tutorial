# Polymorphism:- Polymorphism is a combination of two greek word. 
# poly means many 
# morph means forms  
# Polymorphism in python is an ability of python object to take many forms.
# If a variable , object , method performs different behaviour according to situation is called as polymorphism.
# There are four types of polymorphism. 
# 1) Duck Typing 
# 2) Operator Overloading 
# 3) Method Overloaing 
# 4) Method Overriding

# 1):- Duck typing :- Duck typing in python is a programming concept where the type or the class of an object is less
# important than the methods it defines. When we use duck typing , you do not check types at all. Instead, you check  
# for the presence of a given method or attribute. 

class ide: 
    def execute(self): 
        print("Our programm is executing.") 
    def run(self): 
        print("Execute successfuly.") 
    def compile(self): 
        print("Compilation has been successfully completed.") 
class vscode: 
    def output(self,other): 
        other.execute()
        other.run()
        other.compile() 
v1 = vscode() 
e2 = ide()  
v1.output(e2)   


class duck: 
    def walk(self): 
        print('thapak thapak thapak') 
    
class horse: 
    def walk(self): 
        print('tabdak tabdak tabdak')  

def myfunction(obj): 
    obj.walk() 

d = duck() 
myfunction(d) 

h = horse() 
myfunction(h)


