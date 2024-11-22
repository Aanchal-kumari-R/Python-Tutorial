'''Access Specifier/Modifier :- Access specifier and access modifier in python programming are used to limit the access of class 
 variables and class methods outside of class while implementing the concepts of inheritance. ''' 

'''There are three types of access specifier:- 
1):- Public Access Specifier 
2):- Private Access Specifier 
3):- Protected Access Specifier''' 

'''Public Access Specifier:- All the variables and methods (member function) in python are by default public. Any instance variable
in a class followed by the 'self' keyword. i.e. self.var_name are public accessed.'''

class Students: 
    def __init__(self,name,age): 
        self.name = name 
        self.age = age 

    def show(self): 
        print(f"The name of student is {self.name} and age is {self.age}.") 

students = Students("Aanchal Singh",23) 
students.show() 
print(students.name) 
print(students.age) 
