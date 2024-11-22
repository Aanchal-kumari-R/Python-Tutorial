''' Private Access Specifier:- By definition, private member of a class(variables and methods) are those members which are  
only accessible inside the class. We can not use private members outside of class. 
However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name 
with a double underscore(__). This is known as "weak internal use indicators." ''' 

# class Geek: 
#     __name = None  
#     __roll = None 
#     __branch = None 

#     def __init__(self,name,roll,branch): 
#         self.__name = name 
#         self.__roll = roll 
#         self.__branch = branch 

#     def __privateFunction(self): 
#         print("Name :",self.__name) 
#         print("Roll ",self.__roll) 
#         print("Branch :",self.__branch) 

#     def accessprivateFunction(self): 
#         self.__privateFunction() 


# obj = Geek("Aanchal Singh",12,"Information Technology") 
# obj.accessprivateFunction()    

class students: 
    def __init__(self,age):
        self.__age = 23  

    def __func(self): 
        print(self.__age)


obj = students(21) 

# print(obj.__age)  # cannot be accessed directly
# obj.__func() 
print(obj._students__age) #can be accessed indirectly 
obj._students__func()

  