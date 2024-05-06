#Write a programm to print characters present at even index and odd index seperatelly for the given String.  
# 1st way
str = input("Enter any String :") 
i = 0 
print("The even index of String character is:") 
while i<len(str): 
    print(str[i]) 
    i = i+2 
print("The Odd index of String character is:")  
i = 1
while i<len(str): 
    print(str[i]) 
    i = i+2  

#2nd way 
str = input("Enter the String:") 
print("The character present at even index is:",str[0::2]) 
print("The character present at odd index is:",str[1::2]) 