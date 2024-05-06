import random 

# random randint() method 
print(random.randint(2,9))  

# random randrange() method 
print(random.randrange(1,9))  

# random choice() method 

l = ["apple","banana","cherry"]
print(random.choice(l))  

# random() method 
print(random.random()) 

# shuffle() method 
l = [10,20,30,40]  
random.shuffle(l) 
print(l)  

# uniform() method 

u = random.uniform(3,9) 
print(u)