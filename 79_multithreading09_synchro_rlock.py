''' RLock Thread Synchronization:- A reentrant lock is a Synchronization primitive that may be acquire multiple times by the 
same threads. A reentrant lock, must be realesed by the thread that acquire it. '''
from threading import * 
class Flight: 
    def __init__(self, available_seat): 
        self.available_seat = available_seat  
        self.l = RLock() 
        # print(self.l)
    def reserved(self, need_seat):  
        self.l.acquire() 
        self.l.acquire() 
        # print(self.l)
        print("Available Seats:", self.available_seat ) 
        if(self.available_seat >= need_seat): 
            name = current_thread().name 
            print(f"{need_seat} seat is alloted for {name}") 
            self.available_seat -= need_seat  
        else: 
            print("Sorry all seats has alloted.") 
        self.l.release() 
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

