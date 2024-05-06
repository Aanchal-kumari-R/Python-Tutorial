num = int(input("Enter a number to check polindromic number or not: "))  
df = num 
temp = 0 
while num>0: 
    rem = num % 10 
    temp = temp*10 + rem 
    num //=10 
if df == temp: 
    print(df, "is Polindromic number. ")  
else: 
    print(df, "is not Polindromic nubmer. ")
 
 
n= input("Enter a Number to Check polindromic or Not :- ")

if n == n[::-1]:
  print(n,' is Polindromic String')
else:
  print(n,' is Not Polindromic String')