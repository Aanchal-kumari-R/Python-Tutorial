"Random Method:- Python random module generates random number in python."
import random 

# random randint() method :- Return a number between 5 and 10 (both included).
print(random.randint(5,10))  

# random randrange() method ;- Return a number between 3(included) and 9(not included)
print(random.randrange(3,9))  

# random choice() method :- Return a random element from the list.

l = ["apple","banana","cherry"]
print(random.choice(l))  

# random() method :- random() method return a random float number between 0 and 1.
print(random.random()) 

# shuffle() method :- This method take a sequence and return a sequence from in a random order.
l = [10,20,30,40]  
random.shuffle(l) 
print(l)  

# uniform() method :- Return a floating point number between two given parameters.

u = random.uniform(3,9) 
print(u)