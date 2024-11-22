"""Accept the marks of English, math , science and social studies subject and display the stream alloted according to following:- 
All subject more than 80 marks                  science stream 
English > 80 and math ,science above 50         Commerce stream  
English < 80 and social studies >80                 Humanities """ 

math = eval(input("Enter the marks of math :- "))
English = eval(input("Enter the marks of english :- "))
Science = eval(input("Enter the marks of science :- "))
social_studies = eval(input("Enter the marks of social studies :- ")) 

if math>80 and English>80 and Science>80  and social_studies>80: 
    print("Science Stream") 

elif English>80 and math>50 and Science>50: 
    print("Commerce Stream") 

elif English<80 and social_studies >80: 
    print("Humanities")