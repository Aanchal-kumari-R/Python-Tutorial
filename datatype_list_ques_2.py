#Write a python program to count number of items having list as value in dictionary 
list1 = {'jay':['male',23,12000],'Ram':["male",23,20000],'Shyam':30,'Raj':["ram",23,22200]} 
count = 0 
for item in list1: 
    if  isinstance(list1[item],list): 
        count +=1 
print(count)