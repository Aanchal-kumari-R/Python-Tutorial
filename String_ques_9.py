#Write a programm for the following requirment 
#input:a4b3c2 
#output:aaaabbbcc 

str = "a4b3c2" 
output = "" 
for ch in str: 
    if ch.isalpha(): 
        x = ch 
    else: 
        d = int(ch) 
        output = output+x*d 
print(output)