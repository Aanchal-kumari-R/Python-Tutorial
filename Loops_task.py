#num1 = eval(input("Dear user, Enter a number from where you start the table:"))  
#num2 = eval(input("Dear user, Enter a number from where you end the table :"))  

"""for num in range(num1,num2):  
    if num%2 == 0:  
        j = 1 
        while j<=10:  
           print(f"{num}*{j}= {num*j}", end ="\t")  
           j+=1   
        print("")  """


"""num1 = eval(input("Dear user, Enter a number from where you start the table:"))  
#num2 = eval(input("Dear user, Enter a number from where you end the table :"))  

j = 1 
while j<=10: 
    for num in range(num1,num2): 
        if num%2 == 0: 
            print(f"{num}*{j}= {num*j}", end ="\t") 
    j+=1 
    print(" ") """

num1 = eval(input("Dear user, Enter a number from where you start the table:"))  
num2 = eval(input("Dear user, Enter a number from where you end the table :"))   

j = 1 
while j<=10: 
     i = num1 
     while i<=num2:  
        if i%2 == 0:    
          print(f"{i}*{j} = {i*j}",end ="\t") 
        i+=1 
     print(" ")   
     j+=1      

 
