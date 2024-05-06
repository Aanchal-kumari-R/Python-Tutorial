n = eval(input("Enter the  number : "))
sum = 0 
if(n%2==0) : 
    for i in range(0,n,2):
        sum = sum+i  
    print("Sum of even range is : ",sum) 

else:   
    for i in range(1,n,2):
      sum = sum+i
    print("Sum of odd range is :",sum)

 
