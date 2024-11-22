# x = int(input("Enter any number to match the match cases :- ")) 
# match x : 

#     case 0: 
#         print("x is zero.") 

#     case 4: 
#         print("x is four.") 

#     case 8: 
#         print("x is Eight.") 

#     case _: 
#         print("x is default.",x) 


x = int(input("Enter any number to match the match cases :- ")) 
match x : 

    case 0: 
        print("x is zero.") 

    case 4: 
        print("x is four.") 

    case 8: 
        print("x is Eight.") 

    case _ if x!=90: 
        print("x is not ninety.",x) 
    case _ if x!=80: 
        print("x is not eighty.",x) 
    case _: 
        print("x is default.",x) 
