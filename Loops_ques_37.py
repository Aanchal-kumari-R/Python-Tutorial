"""Write a programm to print the following series:-  
1--49 
2--48 
3--47 
4--46 
.... 
.... 
.... 
.... 
48--2 
49--1""" 

i = 1  
j = 49
while i<=49 and j>=1:  
    print(i ,'--',j ) 
    i+=1 
    j-=1