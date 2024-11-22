x = 20 
y = 10 
if x>y: 
    print(x*y) 
    print("This is if block") 
    print("This is our python class") 

print("This is out of if block") 


#Shorthand if statement  
a = 200 
b = 30
if a > b: print("a is greater than b") 

a = 2 
b = 330 
print("A") if a > b else print("B") 

a = 300 
b = 40 
c = 100 

if a>b and c>b: 
    print("Both conditions are true") 

if b>a or c>b: 
    print("Only one condition is true") 


a = 33 
b = 200 

if not a>b: 
    print("a is not greater than b")  

#Nested If 
    x = 41 
    if x > 10: 
        print("Above ten") 
        if x > 20: 
            print(" and also above twenty") 
        else: 
            print("but not above 50")
            
# pass statement 
if b > a: 
    pass