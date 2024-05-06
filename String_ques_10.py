# Write a programm for the following requirment 
# input:aaaabbbccz 
# output:4a3b2c1z   

str1 = "aaaabbbccz" 
output = "" 
previous = str1[0] 
i = 1 
count = 1 
while i < len(str1): 
    if str1[i] == previous: 
        count =count +1 
    else:  
        output =  output+str(count)+previous 
        previous = str1[i]  
        count = 1 
    if i == len(str1)-1: 
        output = output+str(count)+previous 
        count = 1 
    i = i+1 
print(output)
