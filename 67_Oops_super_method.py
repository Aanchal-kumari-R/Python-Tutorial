# Super() function:- The super() function is a build-in function that returns the objects that 
# represent the parent class. It allows to access the parent class methods and attributes in the  
# child class.

class circle: 
    def __init__(self,r): 
      self.r = r 
      super().__init__(int(input("Enter the length:- ")), int(input("Enter the breath:- "))) 
    def area(self): 
       print("The area of circle is:- ", 3.14 * self.r **2) 
       super().area() 

class rectangle: 
   def __init__(self,l,b): 
      self.l = l 
      self.b = b 
   def area(self): 
      print("The area of rectangle is:- ", self.l *self.b) 

class square(circle,rectangle): 
   def __init__(self, x): 
      self.x = x
      super().__init__(x) 
   def area(self): 
      print("The area of square is:-", self.x *self.x)  
      super().area()  
obj = square(12)  
obj.area()


class employee: 
   def __init__(self,name,id): 
      self.name = name 
      self.id = id  
   def info(self): 
      print(self.name,self.id)
class programmer(employee): 
   def __init__(self,name,id,lang): 
      super().__init__(name,id) 
      self.lang = lang   
   def info(self): 
      print(self.name, self.id, self.lang) 
      super().info()     
obj = programmer("Aanchal",234,"Python")  
obj.info()
# print(obj.name)
# print(obj.id)
# print(obj.lang)