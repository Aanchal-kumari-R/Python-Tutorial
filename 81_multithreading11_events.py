'''Thread Communication Event:- This is one of the simplest mechanism for communication between threads:  
* One thread signals an event and other threads wait for it. 
* An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() 
method. The wait() method blocks until the flag is true. 
* The flag is initially false.'''

'''Events Methods(): 
* set() method:- It set the internal flag to true. All threads waiting for it to become true are awakened. Threads that call wait() 
one the flag is true will not block at all.  

* clear() method:- It reset the internal flag to false. Subsequentlgy. Threads calling wait() will block untill set() is called to 
set the internal flag to true again.  

* is_set() method:- nIt return true if only and if the internal flag is true. 

* wait() method:- It block until the internal flag is true. If the internal flag is true on entry, return immediately. Otherwise, 
block until another thread calls set() to set the flag to true, or until the optional timeout occurs. '''
from threading import Thread, Event 
from time import sleep 

def light_switch(): 
    sleep(3) 
    e.set() 
    print("Green Light ON.\n") 
    sleep(5)  
    print("Red Light ON.") 
    e.clear() 

def traffic(): 
    e.wait() 
    while e.is_set(): 
        print("You can go.") 
        sleep(.5) 
    sleep(1)  
    print("Program Done!")
      
e = Event()  

t1 = Thread(target=light_switch) 
t2 = Thread(target=traffic) 

t1.start()
t2.start()   
















