'''Creating a thread by creating a child class to thread class ;-  
* We can create our own thread child class by inheriting thread class from threading module. 
* Methods: 
*run(): Every thread will run this method when thread is started. we can override this method and write our  
own code as body of the method. A thread will terminate automatically when it comes out of the run method. 
*join(): This method is used to wait till the thread completely executes and run() method.
'''

from threading import Thread 
# class myThread(Thread): 
#     pass 

# t = myThread() 
# print(t.name)  

# class Mythread(Thread): 
#     def run(self):  
#         for i in range(5):
#           print("Child Thread") 

# t = Mythread() 
# t.start()  
# t.join()
# for i in range(5): 
#    print("Main Thread")

'''Creating a thread by inheriting thread class and passing arguments to the constructor of child class ;-'''

# class myThread(Thread): 
#   def __init__(self,a):  
#     Thread.__init__(self)  
#       print("Child thread class.",a) 
#       self.a = a  
# t = myThread(10) 
# t.start() 
 
#   print("Main Thread") 

class mythread(Thread): 
    def __init__(self,a): 
        Thread.__init__(self)  
        self.a = a 
        print("Child thread class,",a) 
t = mythread(10) 
t.start() 
print("Main Thread")