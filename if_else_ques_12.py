"""Accept any city from the user and display monument of that city. 
City                             Monument 
Delhi                            Red Fort 
Agra                             Taj Mahal 
Jaipur                           Jal Mahal""" 

city_name = input("Enter the name of the city:- ") 
if city_name.lower() == 'delhi': 
    print('Red Fort') 

elif city_name.lower() == "agra": 
    print("Taj Mahal") 

elif city_name.lower() == "jaipur": 
    print('Jal Mahal') 

else: 
    print('Enter correct city name.')