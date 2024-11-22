# Static Method :- Static methods are used when some processing is related to the class but does not need the class or 
#  it instance to perform any work. We used static method when we want to pass some values from outside and perform some  
# action in the method. Decorator @staticmethod need to write above the static method.   
# In statice method , if we use self keyword as a first parameter in the method then we get an error.

class employee:
  @staticmethod 
  def calc(): 
    n1 = eval(input("Enter 1st number:- ")) 
    n2 = eval(input("input 2nd number:- "))
    print(f"Addition = {n1+n2} , subtraction = {n1-n2}") 
df1 = employee() 
df1.calc()  

class mobile:
  @staticmethod  
  def show_model(m,p): 
    model = m 
    price = p 
    print(f"Model = {model} , Price = {price}")  
realme = mobile() 
mobile.show_model("Realme X", 1000)    