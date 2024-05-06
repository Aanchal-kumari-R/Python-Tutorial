#write a programm to sort character of the string, first alphabet symbols followed by digit

str = input("Enter some alphanumeric String to sort:")  
alphabets = [] 
digit = [] 
for ch in str: 
    if ch.isalpha(): 
        alphabets.append(ch) 
    else: 
        digit.append(ch) 
output = "".join(sorted(alphabets)+sorted(digit)) 
print(output)