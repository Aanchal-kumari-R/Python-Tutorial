'''** Set and Get Thread Name:  
* current_thread():- This function return current thread object. 
* name property:- This property is used to set and get the name of thread.   ''' 
 
from threading import Thread , current_thread 

# def disp(): 
#   print("default child thread name :",current_thread().name) 
#   current_thread().name = "Doc Thread" 
#   print("New Child thread name :",current_thread().name) 
# t = Thread(target=disp) 
# t.start() 

print(" default Main thread Name ", current_thread().name) 
current_thread().name='GeekyShows Thread '
print(" New Main thread Name " , current_thread().name)  



