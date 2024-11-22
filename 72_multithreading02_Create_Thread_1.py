''' ** Creating thread without using class :  
from threading import Thread  
thread_object = Thread(target = function_name,args=(args,args2...)) 
* thread _object = It represent our thread. 
* target = It represent the function on which the thread will act. 
* args = It represent a tuple of arguments which are passed to the function. 
t = Thread(target = disp, args = (10,20))  

** Start Thread :- Once a thread is created it should be started by calling start() method.'''

# from threading import Thread 
# def disp(): 
#     print("Thread Running.") 
# t = Thread(target=disp) 
# t.start()   

# start multiple time thread   
# def disp(a,b): 
#     print("Thread is running..",a,b) 
# for i in range(5): 
#     t = Thread(target=disp,args=(10,20)) 
#     t.start() 
    
# def disp():  
#     for i in range(5):
#        print("Child Thread\n")  
# t = Thread(target=disp) 
# t.start()  

# for i in range(5): 
#    print("Main Thread") 


