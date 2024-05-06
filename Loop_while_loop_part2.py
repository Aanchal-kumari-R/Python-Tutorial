print("Horizontal Table")
i = 10 
while i<=20: 
    j = 1 
    while j<=10: 
        print(i*j,end="\t") 
        j+=1  
    print(" ")
    i+=1   
    
print("Vertical Table")
j = 1 
while j<=10: 
    k = 10 
    while k<=19: 
        print(f"{k}*{j}= {j*k} ",end =" \t ") 
        k+=1 
    print("") 
    j+=1
    

n1 = eval(input("Dear user, Enter a number where you want start there:")) 
n2 = eval(input("Dear user,Enter a number where you want end the table:")) 

while n1<n2:  
    j = 1 
    while j<=10:  
          print(f"{n1}*{j}= {n1*j} " , end = " \t ") 
          j+=1 
    print(" ") 
    n1+=1  

n1 = eval(input("Dear user, Enter a number where you want start there:")) 
n2 = eval(input("Dear user,Enter a number where you want end the table:")) 

j = 1 
while  j<=10 :  
    n = n1  
    while n<n2:  
          print(f"{n}*{j}= {n*j} " , end = " \t ") 
          n+=1 
    print(" ") 
    j+=1