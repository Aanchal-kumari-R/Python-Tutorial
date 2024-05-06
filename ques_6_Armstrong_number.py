num = int(input("Enter any number to chech given number is Armstrong number:")) 
arms = 0 
power = len(str(num))
temp = num 
while num>0: 
    rem = num%10 
    arms = arms+rem**power 
    num = num//10 
if temp == arms: 
    print(temp, "is Armstrong Number:") 
else: 
    print(temp,"is not Armstrong number:")