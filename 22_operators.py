##Arithmetic operator 
x = 5 
y = 3 
print(x+y)  
print(x-y)
print(x*y) 
print(x**y) 
print(x/y)
print(x//y) 
print(x%y)  
print(-3%10) 
print(-3/10)
 
##Assignment operator 
x = 5 
print(x)  
x=5
x +=5 
print(x)  
x=5
x -= 5  
print(x) 

x=5 
x *=5 
print(x) 

x=5 
x =3 
print(x)  

x=5 
x %= 5 
print(x) 

x=5
x //= 5 
print(x)  
 
x = 5
x **= 5 
print(x)    

##Relational operator   
n1 = 12 
n2 = 20 
print(n1==n2) 
print(n1!=n2) 
print(n1>n2) 
print(n1<n2)
print(n1<=n2) 
print(n1>=n2)

##Logical Operator    
n1 = 20 
n2 = 10 
n3 = 40  

# Logical and operator
print(n1>n2 and n3>n2) 
print(n1<n2 and n3>n2)   
print(n1>n2 and n2>n3)
print(n1<n2 and n2>n3)  

df1 = 79 
df2 = 0 
print(df1 and df2)    

#if x is true then it return y , otherwise it returns x  
x = 56 
y = 12 
print(x and y)  
print(y and x)  

x1 = 0 
y1 = 5 
print(x1 and y1) 
print(y1 and x1)   

num1 = 0 
num2 = " " 
print(num1 and num2) 
print(num2 and num1)

# Logical or operator  
print(n1>n2 or n3>n2) 
print(n1<n2 or n3>n2)   
print(n1>n2 or n2>n3)
print(n1<n2 or n2>n3)   

# if x is true then it returns x , otherwise it returns y 
n1 = 20 
n2 = 0  
print(n1 or n2)   
print(n2 or n1)  

num1= '' 
num2 = 0 
print(num1 or num2) 
print(num2 or num1)

# Logical not operator 
print(not(n1<n2 and n3>n1 or n1!=n2))  

##Bitwise Operator     
#Bitwise complement operator
n1 = 5 
print(~n1) 

n2 = -4 
print(~n2)  

#Bitwise and operator(&)  
n1 = 8 
n2 = 9 
print(n1 & n2) 

z = 4 
print(n1 & z) 

print(bin(4)) 
print(bin(10))  

#Bitwise or operator(|) 
n1 = 8 
n2 =9 
print(n1 | n2) 

n3 = 4 
print(n1 & n3)  

#Bitwise left shift operator  
n1 = 9 
print(n1<<2) 
print(n1<<3)  

#Bitwise Right shift operator 
print(n1>>2) 
print(n1>>3)

#Bitwixe x-or operator (1^1=0) 
n1 = 8 
n2 = 9 
print(n1^n2)  

##Membership operator 
#in membership operator 
df = "Samarachand" 
print("Z" in df) 
print("S" in df)
print("C" in df)  

#not in membership operator 
df = "Samarachand" 
print("S" not in df) 
print("C" not in df) 

##Identity operator  
df1 = 89 
df2 = 99 
#is identity operator
print(df1 is df2) 
df3 = 89 
print(df1 is df3)   

n1 = [11,22,33,44] 
n2 = n1 
n3 = n1[:] 
print(n1 is n2) 
print(n1 is n3)

#is not identity operator 
df1 = 89 
df2 = 99 
print(df1 is not df2)  
df3 = 99 
print(df2 is not df3)



