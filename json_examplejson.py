import json 

# convertiong python object to json
d = { 
    'course' : "Python", 
    'fee' : 14000 
} 

f = json.dumps(d) 
print(f) 

# converting json data to python object  

d1 = '{"course": "Python",  "fee" : 33200, "duration" : "2 months"}' 
x = json.loads(d1)  
print(type(x))
print(x)