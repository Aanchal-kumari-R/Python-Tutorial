import datetime 
x = datetime.datetime.now() 
print(x)  

d = datetime.datetime(2001,2,15) 
print(d)  

b = datetime.datetime.now() 
now = b.strftime("%y") 
print(now)