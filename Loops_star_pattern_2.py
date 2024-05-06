print("Pattern 1")
for i in range(1,6): #row
    for j in range(1,i+1): #column 
        print("*", end = " ")  
    print("") 

print("Pattern 2")

for j in range(5,0,-1): #column
    for i in range(1,j+1): #row
        print("*" , end = " ") 
    print(" ") 

print("Pattern 3")

for i in range(1,6): #row 1
    for j in range(1,6):  #space 
        if j>= 6-i:
          print("*",end = " ")  
        else: 
            print(" ", end = " ")
    print()   

print("Pattern 4")

for j in range(1,6): 
    for i in range(1,6): 
        if i>=j : 
            print("*", end = ' ') 
        else: 
            print(" ", end = ' ') 
    print()   

print("Pattern 5")

for i in range(5): 
    for j in range(5): 
        print("*", end = " ")  
    print("")

print("Pattern 6")

for i in range(1,6):
    for j in range(1,6): 
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*" , end = " ") 
        else: 
            print(" ",end = ' ')
    print("")  

print("Pattern 7")

i = 1
while i<= 5 : 
    j = 1 
    while j <= 5: 
        if i == 1 or i == 5 or j == 1 or j == 5: 
          print("*", end = " ")      
        else:                        
          print(end = "  ")   
        j=j+1  
    print(" ")  
    i=i+1

print("Pattern 8")


for i in range(1,6): 
    for j in range(1,i+1): 
        print(j, end = " ") 
    print(" ")  

print("Pattern 9")

for i in range(1,6): 
    for j in range(1, i+1): 
        print(i , end = " ") 
    print(" ") 
 
print("Pattern 10")

count = 0
for i in range(1,6): 
    for j in range(1,i): 
        count= count+1
        print(count,end = " ") 
    print(" ") 

print("Pattern 11")

for i in range(65,69): 
    for j in range(65,i+1): 
        print(chr(j), end = " ") 
    print("") 

print("Pattern 12")

for i in range(65,69): 
    for j in range(65,i+1): 
        print(chr(i), end = " ")
    print(" ")  

print("Pattern 13")

n = 5 
num = 65 

for i in range(0,n): 
    for j in range(0,i+1): 
        ch = chr(num) 
        print(ch, end = " ") 
        num = num+1  
    print("")   

print("Pattern 14") 

for i in range(0,6): 
    for j in range(0,6-i-1): 
        print(" ", end = "") 
    for k in range(0,i+1): 
        print("*",end = " ") 
    print(" ") 
        
for i in range(0,6-1): 
    for j in range(0,i+1):  
        print(" ", end = "") 
    for k in range(0,6-i-1): 
        print("* ", end = "") 
    print()

print("Pattern 14") 

a = 1 
b = 5 
 
for k in range(0,2*b): 
    if k<4:
        print(('* '*a))
        a = a+1 
    else: 
        print('* '*a) 
        a = a-1 
