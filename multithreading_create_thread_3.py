# creating a thread without using a child class to thread class  
from threading import Thread  
class myThread: 
    def disp(self,a,b): 
        print(a,b) 

myt = myThread() 
t = Thread(target=myt.disp, args=(10,20)) 
t.start()