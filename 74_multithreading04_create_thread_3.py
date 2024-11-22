# creating a thread without using a child class to thread class 
''' We can create an independent thread child class that does not inherit from Thread class  
    from threading module.'''  
 
from threading import Thread 

class myThread: 
    def disp(self,a,b): 
        print(a,b) 

myt = myThread() 
t = Thread(target=myt.disp, args=(10,20)) 
t.start() 
