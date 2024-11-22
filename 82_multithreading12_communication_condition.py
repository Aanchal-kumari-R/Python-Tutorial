""" Condition:- Condition class is used to improve speed of communication between threads, The Condition class object is called  
Condition variable. A Condition variable is always associated with some kind of lock. A condition is a more advanced version of 
the event object. """ 

'''Conditon Method: 
* notify(n=1):- This method is used to immediately wake up one thread waiting on the condition. Where n is number of thread need 
to wake up. 

* notify_all():- This method is used to wake up all threads waiting on the condition. 

* wait(timeout = None):- This method wait until notified or intil a timeout occurs. '''
from threading import Thread, Condition 
from time import sleep  

lst = [] 

def produce(): 
    cv.acquire() 
    for i in range(1,6): 
        lst.append(i) 
        sleep(1) 
        print("Item Produce...") 
    cv.notify() 
    cv.release() 

def consume(): 
    cv.acquire() 
    cv.wait(timeout=0) 
    cv.release() 
    sleep(1) 
    print(lst)
cv = Condition() 

t1 = Thread(target=produce) 
t2 = Thread(target=consume) 

t1.start() 
t2.start()