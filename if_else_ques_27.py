"""Accept three sides of triangle and check weather the triangle possible or not ? 
(triangle is possible only when sum of any two sides is greater than 3rd side) """ 

s1 = int(input("Enter the first side of triangle:- "))
s2 = int(input("Enter the second side of triangle:- "))
s3 = int(input("Enter the third side of triangle:- "))  

if (s1+s2)> s3 and (s1+s3)>s2 and (s2+s3)>s1: 
    print("Triangle is possible.") 

else: 
    print("Triangle is not possible.")