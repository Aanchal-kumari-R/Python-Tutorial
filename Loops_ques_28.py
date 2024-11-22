"""Write a programm to print the following series till nth terms. 
1,4,9,16,25...........nth terms""" 

n = int(input("Enter the value of n:- "))
i = 1 
while i <= n: 
    print(i**2, end = ' , ') 
    i+=1