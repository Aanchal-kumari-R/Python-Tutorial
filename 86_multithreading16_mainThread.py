import threading
 
t = threading.main_thread().getName()
print("This is the example of main thread.") 

print(t)