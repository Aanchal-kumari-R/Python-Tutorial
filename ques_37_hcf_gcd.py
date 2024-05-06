x = int(input("Enter the first number:- ")) 
y = int(input("Enter the second number:- ")) 

if x>y: 
    smaller = x 
else: 
    smaller = y 

for i in range(1,smaller): 
    if((x%i == 0) and (y%i == 0)): 
        hcf = i 
print(hcf)