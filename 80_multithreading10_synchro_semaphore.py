''' Thread Synchronization Semaphore and Bounded-Semaphores:- This is one of the oldest synchronization primitive in the history of  
Computer Science, invented by early Dutch computer scientist Edsger W. Dijkstra. 
A semaphore manages an internal counter  which is decremented by the acaquire() call and incremented by each release call.
The counter can never go below zero; when acquire finds that it is zero, it blocks, waiting untill some other thread calls release().
'''

from threading import * 
class Flight: 
    def __init__(self, available_seat): 
        self.available_seat = available_seat  
        self.l = BoundedSemaphore(2) 
        print(self.l)
    def reserved(self, need_seat):  
        self.l.acquire() 
        print(self.l._value)
        print("Available Seats:", self.available_seat ) 
        if(self.available_seat >= need_seat): 
            name = current_thread().name 
            print(f"{need_seat} seat is alloted for {name}") 
            self.available_seat -= need_seat  
        else: 
            print("Sorry all seats has alloted.") 
        self.l.release() 
        # self.l.release() 
f = Flight(2) 

t1 = Thread(target=f.reserved, args=(1,), name = "Rahul") 
t2 = Thread(target=f.reserved, args=(1,), name="Sonam") 
t3 = Thread(target=f.reserved, args=(1,), name="Raj") 


t1.start() 
t2.start()
t3.start() 

# t1.join()
# t2.join()
# t3.join()

# print("Main Thread")

