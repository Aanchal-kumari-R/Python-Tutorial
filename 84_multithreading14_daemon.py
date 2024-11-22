"""Deamon Thread:- A deamon thread is a thread which runs continuously in the background. It provides support to non-deamon threads. 
When last non-daemon thread terminates , automatically all deamon threads will be terminated. We are not require to terminate 
daemon thread explicitly.  """ 

"""Create Deamon Thread:- setDaemon(True) Method or daemon = True Property is used to make a thread a Daemon thread. 
 t1 = Thread(target = disp) 
  t1.setDaemon(True) // depricated
   or 
t1.daemon = True 

setDaemon(True/False):- This method is used to set a Thread as Daemon Thread. If we pass True non-daemon thread will become deamon 
and if false daemon thread will become non-daemon. 

Daemon Property/ daemon:- This property is used to check wheather a thread is daemon or not. It returns true if thread is daemon else false. 
isDeamon() // depricated
"""

# from threading import Thread 

# def disp(): 
#     print("Deamon Thread.") 

# t1 = Thread(target=disp) 
# print("Before Demon :- ",t1.daemon)  
# t1.daemon=True 
# print("After Demon :- ",t1.daemon) 
# t1.start()  
 
"""Main Thread is always non-daemon thread. 
Rest of the threads inherits daemon nature from their parents. 
- If parent thread is non daemon then child thread will become non-daemon thread. 
- If parent thread is daemon then child thread will also become a daemon thread. """
# from threading import current_thread  
# mt = current_thread() 
# print(mt.getName()) 
# print(mt.daemon)  

# Example of non-deamon parent and child
# from threading import Thread,  current_thread 
# def disp():  
#     print("Disp Function.")  

# mt = current_thread() 
# print(mt.name) 
# print("MT :-",mt.daemon)  

# t1 = Thread(target=disp) 
# print("T1 :-",t1.isDaemon()) 
# t1.start()  

# Example of deamon parent and child  

# from threading import Thread, current_thread  
# def disp(): 
#     print("Disp function.")   
#     t2 = Thread(target=show) 
#     print("T2 :- ", t2.isDaemon()) 
#     t2.start()

# def show(): 
#     print("Show function.")

# mt = current_thread() 
# print(mt.getName()) 
# print("mt:- ",mt.isDaemon()) 

# t1 = Thread(target=disp) 
# print("T1 Before :-",t1.isDaemon()) 
# t1.setDaemon(True) 
# print("T1 After :- ",t1.isDaemon())  
# t1.start()
# t1.join()

""" nondaemon thread terminate all daemon thread : when last non-daemon thread terminates , automatically all daemon threads 
will be terminated. We are not require to terminate daemon thread explicitly.
"""

# from threading import Thread, current_thread 
# from time import sleep 

# def teacher(): 
#     for i in range(1,11): 
#         print("Teaching Session", i) 
#         sleep(1) 

# t1 = Thread(target=teacher)  
# t1.setDaemon(True)
# t1.start() 
# sleep(5) 
# print("Exam finished.", current_thread().name)
