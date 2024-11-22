import json 
file = open("jsonpost.json","r") 
x = file.read() 
finaldata = json.loads(x) 
print(finaldata) 