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
