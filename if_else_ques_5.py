"""Write a programm to accept percentage from the user and display the grade according to the following criteria:-  
Marks                              Grade 
>90                                A 
>80 and <=90                       B 
>=60 and <= 80                     C 
below 60                           D """ 

prct = eval(input("Enter the percentage:- ")) 

if prct>=90: 
    print('Grade A') 

elif prct<= 90 and prct>80: 
    print("Grade B")

elif prct<= 80 and prct>60: 
    print("Grade C") 

elif prct <= 60: 
    print("Grade D")