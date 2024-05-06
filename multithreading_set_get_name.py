from threading import Thread , current_thread 

# def disp(): 
#     print("default Child thread Name " , current_thread().getName())  
#     current_thread().setName('Doc Thread ')
#     print(" New Child thread Name " , current_thread().getName())  

# t = Thread(target=disp) 
# t.start() 

# print(" default Main thread Name ", current_thread().getName()) 
# current_thread().setName('GeekyShows Thread ') 
# print(" New Main thread Name " , current_thread().getName())  


# def disp(): 
#     print("default Child  Name " , current_thread().name)  
#     current_thread().name = 'Flying Thread '
#     print(" New Child  Name " , current_thread().name)  

# t = Thread(target=disp) 
# t.start() 

# print(" default Main  Name ", current_thread().name) 
# current_thread().name='Geeky Thread ' 
# print(" New Main  Name " , current_thread().name)  

def disp(): 
  pass
t = Thread(target=disp) 
print("Default",t.getName())  
print(t.name)
t.setName("Doc Thread")
print("New ",t.getName())
