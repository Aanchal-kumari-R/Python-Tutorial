# Errors  

# 1st : Compile Time (Syntax) Error :-  
# n1 = 10 
# if n1<20  // here is not indentation
#   print(n1) 

# 2nd :Run-Time (exceptions) Error :-  
# n1 = int(input("Enter 1st number:-")) 
# n2 = int(input("Enter 2nd number:-"))   // in 2nd input we do enter string that why it gives run time error
# add = n1+n2 
# print(add)  

# 3rd: logical error :- 
def increment(sallary): 
    sallary = sallary * 0.1 
    return sallary 
print(increment(36000)) # here output soul be 396000 because we increment 10% in sallary but output is 3600.0 logic in code is wrong  
 
# Exception Handling    

try :
  n1 = eval(input("Enter 1st number:- ")) 
  n2 = eval(input("Enter 2nd number:- ")) 
  add = n1+n2 
except: 
   print("Something went wrong, please try again.") 
else: 
   print("Addition = ",add) 
finally: 
   print("Executed Succesfully........") 

try :
  n1 = int(input("Enter 1st number:- ")) 
  n2 = int(input("Enter 2nd number:- ")) 
  add = n1+n2  
  sub = n1-n2 
  mult = n1*n2 
  div = n1/n2  

except ValueError as df:  
   print("invalid input, Please enter a valid Number.",df) 

except ZeroDivisionError as er:  
    print(f"Addition = {add}, Subtraction = {sub}, Multiplication = {mult}",er)

    print("Division by zero can't possible , please input a number greater than zero.")
except: 
   print("Something went wrong, please try again.") 
else: 
   print(f"Addition = {add}, Subtraction = {sub}, Multiplication = {mult}, Division = {div}")
finally: 
   print("Executed Succesfully........")