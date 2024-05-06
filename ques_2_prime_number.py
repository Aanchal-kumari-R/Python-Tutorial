num = int(input("Dear user,Enter any number to check prime number :- "))  
i = 2  
if num>1: 
  while i<= num//2:  
     if num%i == 0: 
        print(num,"is not prime Number.") 
        break 
     i+=1 
  else: 
     print(num,"is prime Number.")  
else:  
   print(num,"Invalid Number")
   
