#Encapsulation with private access modifier
class Person: 
    def __init__(self,name,age): 
        self.__name = name 
        self.__age = age 

    def display_info(self): 
        print(f"The person name is {self.__name} and age is {self.__age}")

person = Person("Aanchal Singh",23) 
person.display_info()  

#Encapsulation with protected access modifier 
class Person: 
    def __init__(self,name,age): 
        self.name = name 
        self.age = age 

class Students(Person): 
    def __init__(self,name,age): 
        super().__init__(name,age) 

    def print_info(self): 
        print(f"The person name is {self.name} and age is {self.age}") 

students = Students("Goldi Singh",23) 
students.print_info()