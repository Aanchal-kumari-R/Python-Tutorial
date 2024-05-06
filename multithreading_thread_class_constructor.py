from threading import Thread  
class myThread(Thread): 
  def __init__(self,a):  
    Thread.__init__(self)
    print("Child thread constructor.",a) 

def run(self): 
   pass  

t = myThread(10) 
t.start()

print("Main Thread")