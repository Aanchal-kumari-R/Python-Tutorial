#Write a programm to print the frequency of word in String
str = input("Enter the String:")  
#Sheena loves mango and apple. Her sister also loves eating apple and mango.
li = str.split() 
d ={} 

for i in li: 
    if i not in d.keys(): 
        d[i] = 0 
    d[i] = d[i]+1 
print(d)