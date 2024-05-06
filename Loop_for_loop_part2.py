df1 = [[11,22,33,44],(10,20,30,40),{1011:"Ram",1012:"Shyam",1013:"Mohan"},{11,22,33,44}] 
for i in df1: 
    print(i)  

for i in df1: 
    for j in i: 
        print(j) 

df1 = [[11,22,33,44],(10,20,30,40),{1011:"Ram",1012:"Shyam",1013:"Mohan"},{11,22,33,44},88,789] 
for i in df1: 
    if type(i)!= int and type(i)!= float and type(i)!= complex: 
        for j in i:  
            if j%2 == 0:
              print(j,"is even number")  
            else: 
              print(j,"is odd number:")     
    else: 
        print(i)  
        print("\n")  

df1 =  [[11,22,33,44],(10,20,30,40),{1011:"Ram",1012:"Shyam",1013:"Mohan"},{11,22,33,44},88,789]  
for i in df1:  
        if type(i)!= int and type(i)!= float and type(i)!= complex:  
            if type(i)== list or type(i)== tuple or type(i)== str:  
                for k,l in enumerate(i): 
                    print(k,l) 
            elif  type(i)== dict: 
                for n,m in i.items(): 
                    print(n,m) 
            else: 
                for m in i: 
                    print(m) 
        else: 
            print(i) 
        print("\n")

df1 = [11,22,33,44,55,66,77,88] 
num2 = [f"{i} Even" if i%2==0 else f"{i} Odd" for i in df1] 
print(num2)

df2 = [11,22,33,44,55,66,77,88,99,10] 
dt = [f"{i} liest between 20 and 30"  if i >20 and i<30 else f"{i} greater than 30" for i in df2] 
print(dt)

n = input("Enter two number:") 
print(n) 

n1,n2 = [i for i in input("Enter two number seprate with comma(,):-").split(",")]
print(n1,n2)