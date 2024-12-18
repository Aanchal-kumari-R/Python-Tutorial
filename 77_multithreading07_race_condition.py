''' Thread Race Condition:- Race condition is a situation that occurs when thread are acting in an unexpected sequence. thus leading to unrealible output. 
This can be eliminated using thread synchronization.'''
from threading import Thread, current_thread 

class Flight:
  def __init__(self,available_seat): 
    self.available_seat = available_seat 

  def reserved(self,need_seat):  
     print("Available Seat : ", self.available_seat) 
     if(self.available_seat >= need_seat): 
        name = current_thread().name  
        print(f"{need_seat} seat is alloted for {name}" )
        self.available_seat = self.available_seat - need_seat 

     else: 
        print(" Sorry! All seats has alloted.") 

f = Flight(1) 
t1 = Thread(target = f.reserved , args= (1,), name = "Rahul") 
t2 = Thread(target = f.reserved, args = (1,), name = "Sonam") 
t1.start() 
t2.start()
