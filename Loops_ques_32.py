"""Write a programm to find the sum of following series:-  
1 + 2 + 6 + 24 + 120 +.................n terms""" 


n = int(input("Enter the terms:- "))
i = 1 
pr = 1 
sum = 0 

while i<=n: 
    pr = pr * i 
    print(pr,end = " + ") 
    sum = sum + pr 
    i += 1 

print("=", sum)