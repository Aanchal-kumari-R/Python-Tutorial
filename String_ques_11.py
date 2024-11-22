#Write a program for the following requirement: 
#input: a4k3b2 
# output = aeknbd 

str1 = "a4k3b2" 
output = "" 
for ch in str1: 
    if ch.isalpha(): 
        output = output+ch 
        x = ch 
    else: 
        d = int(ch) 
        newch = chr(ord(x)+d) 
        output = output+newch 
print(output)








