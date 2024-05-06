#Remove second largest element from the list 
#1st way
list1 = [12,34,32,35,54,76,87,98] 
list1.sort() 
print(list1[-2],"is the second largest number.")    

# 2nd way
num = [32,34,54,43,23,67,87,88,89] 
largest = num[0]  
sec_largest = num[0]
for i in range(len(num)): 
    if num[i]>largest: 
        largest = num[i]  
for i in range(len(num)): 
    if num[i]>sec_largest and num[i]!=largest: 
        sec_largest=num[i]
print(sec_largest,"is the second largest number.") 