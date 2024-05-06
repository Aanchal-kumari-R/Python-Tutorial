# Write a programm to merge charcaters of 2 Strings into a single String by taking character alternatively  
#ist way:-This method is suitable for same length of Strings
str1 = "RAVI" 
str2 = "TEJA" 
i,j = 0,0 
output = "" 
while i<len(str1) or j<len(str2): 
    output = output+str1[i] + str2[j] 
    i +=1 
    j +=1 
print(output)  

#2nd Way:-This method is suitable for different length of Strings 
str1 = "RAVIKIRAN" 
str2 = "TEJA" 
i,j = 0,0 
output = "" 
while i<len(str1) or j<len(str2): 
    if i<len(str1): 
        output = output+str1[i] 
        i = i+1  

    if j<len(str2): 
        output = output+str2[j] 
        j = j+1  
print(output)  