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