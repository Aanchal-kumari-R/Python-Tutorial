# Write a programm to reverse internal content of each word 
str1 = "Learning python is very good" 
l = str1.split() 
l1 = [] 
for word in l: 
    l1.append(word[::-1]) 
output = " ".join(l1) 
print(output)