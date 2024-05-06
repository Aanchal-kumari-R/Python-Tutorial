num = int(input("Enter any number to print table:- ")) 
i = 0 
while(num>0):  
    print(f"{num} * {i} = ", num*i) 
    i+=1 
    if i ==11: 
        break 
else: 
    print("Invalid number.") 

