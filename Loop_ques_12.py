"""Write a programm to print all even numbers that falls between two numbers (exclusive both numbers) entered from the users using 
while loop.""" 

n1 = int(input('Enter the first number.'))
n2 = int(input('Enter the second number.')) 

while n1<=n2: 
    if n1%2 == 0: 
        print(n1) 
    n1+=1