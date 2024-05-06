# Write a programm to reverse the  content of given string

name = input("Enter any String to reverse String : ") 
output = name[::-1] 
print("Your reverse String is : ",output)   


#reversed() function 
r = reversed(name) 
output = "".join(r) 
print("Your reverse String is : ",output)