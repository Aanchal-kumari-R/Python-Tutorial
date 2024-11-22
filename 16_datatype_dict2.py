#loops in dictionary  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict :
  print(x)    
 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict: 
    print(thisdict[x])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values(): 
   print(x) 

   thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys() :
 print(x)  

 thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.items(): 
   print(x)  

   thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() 
print(mydict)  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict) 
print(thisdict)  

#Nested Dictionary  

myfamily = { 
   "child1":{  
      "name":"Aanchal", 
      "title":"Singh"
   }, 
   "child2":{ 
      "name": "Goldi", 
      "title":"Singh"
   }, 
   "child3":{ 
      "name":"Janki", 
      "title":"Singh"
   }
}  
print(myfamily)  

child1={  
      "name":"Aanchal", 
      "title":"Singh"
} 
child2={ 
      "name": "Goldi", 
      "title":"Singh"
} 
child3= { 
      "name":"Janki", 
      "title":"Singh"
   }

myfamily = {  
   "child1":child1 ,
   "child2":child2 ,
   "child3":child3
   
} 
print(myfamily) 

myfamily = { 
   "child1":{  
      "name":"Aanchal", 
      "title":"Singh"
   }, 
   "child2":{ 
      "name": "Goldi", 
      "title":"Singh"
   }, 
   "child3":{ 
      "name":"Janki", 
      "title":"Singh"
   }
}  
print(myfamily["child1"]["name"])  

#fromkeys 
x ={'keys1','keys2','keys3'}   
y = 0 
thisdict = dict.fromkeys(x,y) 
print(thisdict) 

x ={'keys1','keys2','keys3'}   
thisdict = dict.fromkeys(x) 
print(thisdict)  

#setdefault 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
x = thisdict.setdefault("model","Bronco") 
print(x)  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 

x = thisdict.setdefault("color","white") 
print(x) 
print(thisdict)
 

Emp_data = {'Emp_id':list(range(1011,1016)), 
             'profile':{1011:{'name':'mohan','Desg':'s/w enge','Dept':'it'}, 
                        1012:{'name':'sohan','Desg':'s/w enge','Dept':'it'},  
                        1013:{'name':'Ram','Desg':'s/w enge','Dept':'it'}, 
                        1014:{'name':'Shyam','Desg':'s/w enge','Dept':'it'}, 
                        1015:{'name':'Gita','Desg':'s/w enge','Dept':'it'}}, 

                        'Payment':{1011:{'Gs':25000,'Pf':2000,'SI':23500}, 
                                   1012:{'Gs':50000,'Pf':4000,'SI':26000},
                                   1013:{'Gs':5000,'Pf':500,'SI':4500}, 
                                   1014:{'Gs':250000,'Pf':30000,'SI':225000 }, 
                                   1015:{'Gs':20000,'Pf':2000,'SI':18000}}} 

print(Emp_data)  
print(Emp_data['profile'][1011]['Desg']) 
print(Emp_data['Payment'][1011]['Gs'])