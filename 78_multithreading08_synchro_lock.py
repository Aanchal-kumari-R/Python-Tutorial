''' Thread Synchronization :- Many thread try to access the same object can lead to problems like making data inconsistent or  
getting unexcepted output so when a thread is already accessing an object, preventing any other thread accessing the same object 
is called Thread Synchronization. Thread synchronization is recommended when multiple threads are action on the same object 
simultaneously. There are following technique to do Thread Synchronization: 
1: Using Locks 
2: Using RLock(Re-Entrant Lock) 
3: Using Semaphores''' 

''' 1: Locks:- Locks are typically used to synchronize access to a shared resources. Locks can be used to lock the object in which  
the thread is action. A lock has only two states locked and unlocked. It is created in the unlocked state.  

acquire() method:- This method is used to change the state to locked and returns immediately when the state is locked. 
True:- It blocks until the lock is unlocked the set it to locked and return True. 
False:- It does not block , if a call with blocking set to True would block, return false immediately; Otherwise, set the lock to 
locked and return True.  
Timeout:- When invoked with the floating point timeout argument set to a positive value, block for at most the number of seconds 
specified by timeout and as long as the lock cannot be acquire. 
Release():-  This method is used to release a lock. This can be called from any thread , but only the thread which has acquire the 
lock. There is no return value.''' 

from threading import * 
class Flight: 
    def __init__(self, available_seat): 
        self.available_seat = available_seat  
        self.l = Lock() 
        # print(self.l)
    def reserved(self, need_seat):  
        self.l.acquire(blocking = True, timeout = 2) 
        # print(self.l)
        print("Available Seats:", self.available_seat ) 
        if(self.available_seat >= need_seat): 
            name = current_thread().name 
            print(f"{need_seat} seat is alloted for {name}") 
            self.available_seat -= need_seat  
        else: 
            print("Sorry all seats has alloted.") 
        self.l.release() 
f = Flight(2) 

t1 = Thread(target=f.reserved, args=(1,), name = "Rahul") 
t2 = Thread(target=f.reserved, args=(1,), name="Sonam") 
t3 = Thread(target=f.reserved, args=(1,), name="Raj") 


t1.start() 
t2.start()
t3.start() 

t1.join()
t2.join()
t3.join()

print("Main Thread")

