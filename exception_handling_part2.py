# Manually (Raise) Exception 
# User Define Exception 

try: 
    num = int(input("Enter any number:- ")) 
    if num%2 == 0: 
        pass 
    else: 
        raise Exception 
except ValueError as df: 
    print("Invalid input, please enter a valid number.\n",df)
except: 
    print("Something went wrong, please try again.") 
else: 
    print(num,"is even number.") 
finally: 
    print("Executed Succesfully........")  


try: 
    print("Enter five even number only :- ")  
    df = []  
    for i in range(5): 
        num = eval(input()) 
        if num%2 == 0: 
            df.append(num)  
        else: 
            raise Exception 
except ValueError as df:  
        print("Invalid input, please enter a valid number.\n",df) 

except Exception: 
    print("\nO! O! O!, user you are getting wrong,\nBetter Luck next Luck.\nyou are correct till here.",df[:i+1]) 
else: 
    print("\nnice job, you are really genious\nyour correct answer:-",df)
finally: 
    print("Executed Succesfully........")    


try:  
    name = input("Dear user, enter your name:- ")
    num1 = int(input(f" Dear {name} ,Please enter number which table you want ro write:- ")) 
    tab = [] 
    for i in range(1,11): 
        tab.append(i*num1)  
    print(f" Dear {name} ,Start writting the table:- ") 
    for j in range(10): 
        num = int(input()) 
        if tab[j] == num: 
            pass  
        else: 
            raise Exception 
except ValueError as df:  
    print(f" Dear {name} ,Invalid input, please enter a valid number.\n",df) 

except Exception: 
    print(f"\n Dear {name}, O! O! O!,  you are getting wrong,\nBetter Luck next Luck.\nyou are correct till here.",tab[:j+1]) 
else: 
    print(f"\n Dear {name}, nice job, you are really genious\nyour correct answer:-",tab)
finally: 
    print("Executed Succesfully........")    
