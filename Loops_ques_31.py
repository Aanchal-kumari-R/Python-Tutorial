"""Write a programm to find the sum of following series:-  
1 + 8 + 27 .......n terms""" 

nth_terms = int(input("Enter the value of n:- ")) 

sum = 0
i = 1 
while i<=nth_terms: 
    sum = sum + i**3 
    i+=1  
print(sum) 
 
  
