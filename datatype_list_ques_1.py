# write a programm to delete a duplicate element in list 
#First Way
list1 = ["hello",10,40,30,20,40,20] 
list2 = [] 
for ele in list1: 
    if list1.count(ele)>1 and ele not in list2: 
        list2.append(ele) 
print(list2)         

#Second Way 
l = ["hello",10,30,40,30,20,40,10,40] 
l1 = [] 
for i in range(len(l)): 
    for j in range(i+1,len(l)): 
        if l[i] == l[j] and l[i] not in l1: 
            l1.append(l[i]) 
print(l1)