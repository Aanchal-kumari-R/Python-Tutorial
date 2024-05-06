# from threading import Thread 

# def disp(): 
#     print("Deamon Thread.") 

# t1 = Thread(target=disp) 
# print("Before Demon :- ",t1.isDaemon())  
# t1.setDaemon(True) 
# print("After Demon :- ",t1.isDaemon()) 
# t1.start()  


# # check thread is deamon or not? 

# def disp(): 
#     print("Deamon Thread.") 

# t1 = Thread(target=disp) 
# print("Before: - ", t1.daemon) 
# t1.daemon = True 

# print("After :- ", t1.daemon)  
 
# from threading import current_thread  
# mt = current_thread() 
# print(mt.getName()) 
# print(mt.daemon)  

# Example of non-deamon parent and child
# from threading import Thread,  current_thread 
# def disp():  
#     print("Disp Function.")  

# mt = current_thread() 
# print(mt.getName()) 
# print("MT :-",mt.isDaemon())  

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

# nondaemon thread terminate all daemon thread 

from threading import Thread, current_thread 
from time import sleep 

def teacher(): 
    for i in range(1,11): 
        print("Teaching Session", i) 
        sleep(1) 

t1 = Thread(target=teacher)  
t1.setDaemon(True)
t1.start() 
sleep(5) 
print("Exam finished.", current_thread().name)
