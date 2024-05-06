dayCode = int(input("Enter a number from 0 t0 6 to select the day :- ")) 

match dayCode:  
    case 0: 
        print("Sunday") 
    case 1: 
        print("Monday") 
    case 2: 
        print("Tuesday") 
    case 3: 
        print("Wednesday") 
    case 4: 
        print("Thrusday") 
    case 5: 
        print("Friday") 
    case 6: 
        print("Saturday") 
    case _: 
        print("You have entered wrong number.")





