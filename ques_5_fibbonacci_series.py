num = int(input("Enter any number to print fibbonacci series :")) 
x = 0 
y = 1 
sum = 0 
while(sum<=num):  
    print(sum)
    x = y 
    y = sum 
    sum = x+y  












#2nd way
""" num = int(input("Enter any number:")) 
n1,n2 = 0,1 
sum = 0 
if num<=0: 
    print("Please enter number greater than 0 :") 
else: 
    for i in range(0,num): 
        print(i,end = " ") 
        n1 = n2 
        n2 = sum 
        sum = n1+n2"""
