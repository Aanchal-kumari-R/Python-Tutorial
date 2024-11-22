def calcAdd(num1,num2): 
    "Addition of two number" 
    add = num1+num2 
    print("Addition =",add) 
calcAdd(20,30) 

def even_check(num): 
    "check even number is not" 
    if num%2==0: 
        print(num,"is even number.") 
    else: 
        print(num,"is odd number.") 
even_check(12)  
even_check(19) 



def calc(num1,num2): 
    global add 
    add = num1+num2 
    sub = num1-num2 
    mul = num1*num2 
    div = num1//num2 
    print(f"Addition = {add} Subtraction = {sub} multiplication = {mul} division = {div}") 
calc(22,33)   

print(add)   



def calc(num1,num2): 
    global add ,sub,mul,div
    add = num1+num2 
    sub = num1-num2 
    mul = num1*num2 
    div = num1/num2   
    return add,sub,mul,div
#eee = calc(22,33)   
#print(eee)   
addition, subtraction, multiplication,division = calc(10,20) 
print(addition) 
print(subtraction) 
print(multiplication) 
print(division)

def calc(num1,num2): 
  return num1+num2, num1-num2,num1*num2,num1/num2 
pp = calc(33,367) 
print(pp)   

addition , subtraction, multiplication,division = calc(43,23)  
print(addition) 
print(subtraction) 
print(multiplication) 
print(division)  


def calc(n1,n2): 
    def even(num): 
        if num%2 == 0:  
            print(f"Addition of {n1} and {n2} is even.")  
        else: 
            print(f"Addition of {n1} and {n2} is Odd.") 
    num = n1+n2 
    even(num) 
calc(20,10)

def calc(n1,n2): 
    def even(num): 
        if num%2 == 0: 
            print(f"Addition of {n1} and {n2} is even.") 
        else: 
            print(f"Addition of {n1} and {n2} is odd.")  
    return even(n1+n2)
calc(20,34)


def number(): 
    df = [i for i in range(10,101)] 
    return df 
def check(num): 
    for i in num: 
        if i % 2== 0: 
            print(i, "is even number.")  
        else: 
            print(i,"is odd number.")
check(number())  

def message(name): 
  return name + "How are you ?"   

def status(msg): 
    print(msg) 
     
messa = message("Aanchal ") 
print(messa)  

status(message("Goldi "))

