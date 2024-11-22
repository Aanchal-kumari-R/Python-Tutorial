# 2):- Method Overloading:- Whenever class contains more than one method with same name but different paramenter types 
#  that is called method overloading.
class details: 

  def show(self): 
    print("Welcome") 

  def show(self,firstname=" "): 
    print("Welcome",firstname) 

  def show(self,firstname = " ", lastname = " "): 
    print("welcome", firstname, lastname)  

d1 = details() 
d1.show() 
d1.show("Aanchal") 
d1.show("Aanchal", "Singh")

