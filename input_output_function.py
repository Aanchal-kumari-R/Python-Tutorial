#output() function: print() function is the output funtion 

n1 = 20 
n2 = 10 
add= n1+n2 
print(add) 
print("Addition =" ,add) 
print('Addition of n1 and n2 is',n1+n2) 
print("n1 और n2 का योग है",n1+n2) 
print("Addition of",n1 ,"and",n2, "is",add) 

#format() Function 
print("The sum of {0} and {1} is {2}".format(n1,n2,n1+n2)) 
print("The sum of {1} and {0} is {2}".format(n1,n2,n1+n2)) 
print("The sum of {} and {} is {}".format(n1,n2,n1+n2))  
print(f"The sum of {n1} and {n2} is {n1+n2}") 
print(f"Addition = {n1+n2} Subtraction = {n1-n2} Multiplication ={n1*n2}") 
print(f"Addition = {n1+n2}\n Subtraction = {n1-n2}\n Multiplication ={n1*n2}") 

#input() function: input() is the input function 
num = input("Enter your name :") 
print(num) 
print(type(num))  

num1 = input("Enter your age:")   
print(num1) 
print(type(num1))  

num2 = int(input("Enter your age:")) 
print(num2) 
print(type(num2)) 

num3 = float(input("Enter your percentage:"))
print(num3) 
print(type(num3)) 

#eval() function 
num4= eval(input("Enter your number:")) 
print(num4) 
print(type(num4))  


user = eval(input("Dear user, Enter your name:")) 
print(user)
n1 = eval(input(f"Dear {user} ,Enter your first number:"))  
print(n1)
n2 = eval(input(f" Dear {user} ,Enter your second number:")) 
print(n2) 
print(f"\nDear {user},\nfind the following result:\nAddition = {n1+n2},\nSubtraction = {n1-n2},\nMultiplication= {n1*n2},\nDivision = {n1//n2}")

