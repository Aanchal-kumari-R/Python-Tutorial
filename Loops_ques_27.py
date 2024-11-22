"""Write a programm to print the following series till  nth terms:-  
2 , 22 , 222 , 2222, 22222, ............n terms""" 

n = int(input("Enter value of n :- "))  
st = '2'
i = 0 

while  i < n: 
    print(st,end = " , ")   
    st = st + '2' 
    i = i + 1 
