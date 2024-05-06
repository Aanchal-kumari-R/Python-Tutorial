df = {} 
print(df)  

print(type(df))  
 
df = {101:"Aanchal",102:"Goldi",103:"Janki"} 
print(df)  

print(df.keys()) 
print(df.values())  
print(df[101])  

#Duplicates are not allowed 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#length 
print(len(thisdict))  

#String boolean and list data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}  
print(thisdict)

#dict Constructor() 
thisdict = dict(brand = "Ford",electric = False, year= 1964,
  colors= ["red", "white", "blue"]
) 
print(thisdict)  
 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"] 
print(x) 

#get() 
x = thisdict.get("model") 
print(x)  

#Add new items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()
print(x) 

thisdict["year"] = 2024  
print(x)    

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  
x = thisdict.values()
print(x)
thisdict["colors"] ="red" 
print(x)  

#Get Items 

x = thisdict.items() 
print(x)  

thisdict["color"] = "red" 
print(x)  

#check if key exist 
if "brand" in thisdict :
 print("Yes, brand is in this dictionary")  
 
 #update items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2020 
print(thisdict)  

thisdict.update({"year":2024}) 
print(thisdict) 

#Remove items 
#pop 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") 
print(thisdict)  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.popitem() 
print(thisdict) 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"] 
print(thisdict) 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() 
print(thisdict)  

