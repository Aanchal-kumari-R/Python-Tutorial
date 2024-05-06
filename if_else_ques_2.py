name = input("Enter your name :") 
if len(name)<=3: 
    print(f"Dear  {name}, your name is really nice") 
elif len(name)>3 and len(name)<=5: 
    print(f"Dear {name}, your name is really good") 
elif len(name)>5 and len(name)<=8: 
    print(f"Dear {name}, your name is also good") 
else : 
    dec = input(f"Dear {name}, your name is too much long, if you want then we  recommend name (y/n) :-") 

    if dec == 'y' or dec == "Y":  
        print("What about papu ,kanu,minu,chinu,tinu")
        dec1 = input("Are you satisfied with these name (y/n) :-") 
        if dec1 =='y' or dec1 =="Y": 
            print("Thanks for considering, We became very glad to know this:") 
        else: 
            print(f"Dear {name},we really sorry to delay misunderstanding, your name is amazing") 
    else: 
        print("Thank you for visiting!") 
