"""Accept the following from the user and calculate the percentage of class attended: 
a.    Total number of working days. 
b.    Total number of days for absent. 


After calculating percentage show that, if the percentage less than 75 than student is not able to sit in the exam. """ 

num1 = int(input("Enter the total number of working days:- "))
num2 = int(input("Enter the total number of days for absent:- ")) 

per = (num1-num2)/num1*100
print('Percentage of absent is :- ',per)  

if per <= 75: 
    print("you can not sit in the exam:") 
else: 
    print("You can  sit in the exam:")
