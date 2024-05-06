#Write a programm to print the common characters of two strings

str1 = input("Enter the first String :") 
str2 = input("Enter the second String :") 

s1 = set(str1) 
s2 = set(str2) 
 
str = s1 & s2 
print(str)
