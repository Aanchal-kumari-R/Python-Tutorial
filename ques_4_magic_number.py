num = int(input("Enter a number to check magic number or not:")) 
calc = num 
add = 0 
while num>0: 
    rem = num%10 
    add += rem 
    num //=10 
if calc == add *int(str(add)[::-1]): 
    print(calc,"is magical number.") 
else: 
    print(calc,"is not magical number.")