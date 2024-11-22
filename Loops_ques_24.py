"""Write a programm to accept 10 numbers from the user and display the largest and smallest number.""" 

l = [] 
i = 0 
while i<10: 
    num = int(input("Enter the numbers:- ")) 
    l.append(num) 
    i = i+1 
l.sort() 
print("Largest number is :- ",l[-1]) 
print("Smallest number is :- ",l[0])