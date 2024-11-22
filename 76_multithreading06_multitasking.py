'''Multitasking using a multiple Task:- When multiple task are executed at a time then it is called multi-tasking. for this purpose we need more than one thread ans when we use  
more than one thread , it is called multi threading. '''

from threading import Thread 

class Hotel: 
    def __init__(self,t): 
        self.t = t 
    def food(self): 
        for i in range(1,6): 
            print(self.t,i) 

obj1 = Hotel("Take order from table.") 
obj2 = Hotel("Serve food on table.")  

t1 = Thread(target=obj1.food) 
t2 = Thread(target=obj2.food) 

t1.start() 
t2.start()