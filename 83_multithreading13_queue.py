""" Queue:- The Queue class of queue  module is useful to create a queue that hold the data produced by the producer. 
The data can be taken from the queue and utilized by the consumer. 
We need not use locks since queues are thread safe.""" 

"""Queue Methods:  
* put():- This method is used by producer to insert items into the queue. 
* get():- This method is used by consumer to retrieve items from the queue. 
* empty():- This method returns True if queue is Empty else returns false. 
* full():- This method returns True if queue is full else returns false.  """ 

from threading import Thread 
from queue import Queue 
from time import sleep 

class Produced: 
    def __init__(self): 
        self.q = Queue() 
    
    def produce(self): 
        for i in range(1,6): 
            print("Item produced...",i) 
            self.q.put(i) 
            sleep(1) 

class consumer:
    def __init__(self,prod): 
        self.prod = prod 

    def consume(self): 
        for i in range(1,6): 
            print("Item received..",self.prod.q.get(i)) 

p = Produced() 
c = consumer(p)  

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)  

t1.start()
t2.start()
