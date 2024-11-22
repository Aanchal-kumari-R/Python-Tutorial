# write a program to input a String and print the frequency of the characters 
str = input("Enter your String :") 
content = str.lower() 
 

for i in range(97,123): 
    count=0 
    j = chr(i) 
    for a in content: 
        if j==a: 
            count=count + 1 

    if count > 0: 
                print(j, ":", count)