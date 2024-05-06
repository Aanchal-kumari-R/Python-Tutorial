#Write a programm to reverse the order of words of given String 
str1 = "Learning python is very easy" 
l = str1.split()  
l1 = l[::-1]  
output = " ".join(l1)
print(output)
