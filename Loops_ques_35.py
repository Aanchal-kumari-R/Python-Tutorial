"""Write a programm to print only odd numbers from the given list using while loop. 
L = [23,45,32,25,46,33,71,90]""" 

L = [23,45,32,25,46,33,71,90] 
l = [] 

i = 0 
while i < len(L): 
   if L[i] % 2 != 0: 
      l.append(L[i]) 
   i+=1   
print(l)