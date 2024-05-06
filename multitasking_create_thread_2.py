# Creating a thread by creating a child class to thread class 

from threading import Thread 
# class myThread(Thread): 
#     pass 

# t = myThread() 
# print(t.name)  


class Mythread(Thread): 
    def run(self):  
        for i in range(5):
          print("Child Thread") 

t = Mythread() 
t.start()  
t.join()
for i in range(5): 
   print("Main Thread")