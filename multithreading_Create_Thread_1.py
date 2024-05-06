# Creating thread without using class 

# from threading import Thread 
# def disp(): 
#     print("Thread Running.") 
# t = Thread(target=disp) 
# t.start()  

from threading import Thread
# def disp(a, b):  
#     print("Thread Running ", a , b)   

# for i in range(5):    
#     t = Thread(target=disp, args=(10 , 20)) 

#     t.start()   
   

def disp():  
    for i in range(5):
       print("Child Thread\n")  

t = Thread(target=disp) 
t.start() 

for i in range(5): 
   print("Main Thread")

