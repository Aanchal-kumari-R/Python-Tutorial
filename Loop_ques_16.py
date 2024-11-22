"""  Write a programm to display the number names of the digits of a number entered by the users, for example if the number  
is 231 then output should be two three one.  """  

num1 = input("Enter a numbers:- ") 

l1 = list(num1) 
l2 = len(l1) 
i = 0  

n = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
while i <l2: 
    print(n[int(l1[i])], end = " ") 
    i = i+1  


    