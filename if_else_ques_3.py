name = input("Dear user enter your name:") 
if len(name)<=3: 
    print(f"Dear {name}, your name is really nice.") 
elif len(name)>3 and len(name)<=5: 
    print(f"Dear {name},your name is really good.") 
elif len(name)>5 and len(name)<=8: 
    print(f"Dear {name},your name is also good.") 
else: 
    dec = input(f"Dear {name}, your name is too much long, if you want then we  recommend name (y/n) :-") 

    if dec == 'y' or dec == "Y": 
        print(f"Dear {name}, Thanks for considering, We became very glad to know this::") 
        dec2 = input(f"Dear {name},if you are Male then type (m/M),otherwise you enter (f/F);-")  
        if dec2=='m' or dec2=='M': 
            print(f"Dear {name} you are male, what about papu, kanu ,manu,chonu") 
            dec3 = input("Are you satisfied with these name (y/n) :-") 
            if dec3 =='y' or dec3 =="Y": 
               print("Thanks for considering, We became very glad to know this:") 
            else: 
               print(f"Dear {name},we really sorry to delay misunderstanding, your name is amazing")  
        else: 
            if dec2 =='f' or dec2 =="F": 
                print(f"Dear {name}, you are female, what about pinki,chinki,tinki,tini") 
                dec3 = input("are you satisfied with these name (y/n):-") 
                if dec3 =='y' or dec3 =="Y": 
                    print("Thanks for considering, We became very glad to know this:") 
                else: 
                    print(f"Dear {name}, we really sorry to delay misunderstanding, your name is amazing") 
    else: 
        print("Thank you for visiting!")






         

       