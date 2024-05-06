#write a programm to reverse internal content of every second word present in the given string 
str1 = "One Two Three Fout Five Six" 
list = str1.split() 
i = 0 
list1 = [] 
while i < len(list): 
    if i%2 == 0: 
        list1.append(list[i]) 
    else: 
        list1.append(list[i][::-1]) 
    i = i+1 
    output = " ".join(list1) 
print(output)