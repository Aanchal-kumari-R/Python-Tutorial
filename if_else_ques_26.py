"""Accept three numbers from the users and display the second largest number.""" 

n1 = int(input("Enter the first number:- "))
n2 = int(input("Enter the second number:- "))
n3 = int(input("Enter the third number:- ")) 

if (n1>n2 and n1<n3) or (n1<n2 and n1>n3): 
    print('n1 is the second greatest number:-',n1) 

elif (n2>n1 and n2<n3) or (n2<n1 and n2>n3): 
    print('n2 is the second greatest number:- ',n2) 

elif (n3>n1 and n3<n2) or (n3<n1 and n3>n2): 
    print('n3 is the second greatest number:- ',n3)