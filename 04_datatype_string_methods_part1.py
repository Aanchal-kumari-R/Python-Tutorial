str = "SAMARACHAND" 
print(str)  
# Replace of String
str = str.replace("S","T")  
print(str)  

df1 = "The India"  
df1 = df1.replace("The" ,"Great")  
print(df1)   
df1 = df1.replace(" ","-")  
print(df1)   

str = str.replace("A","B")  
print(str)   

#Concatenation of String
num ="Aanchal "  
num1 = "Singh"   
name  = num+num1  
print(name)   

#Remove space from the String
name1 = " Goldi Singh "  
print(name1.rstrip())  
print(name1.lstrip())  
print(name1.strip())  

#Modification in String
str1 = "There is a king in gurgaon"  
print(str1)     
print(str1.upper())   
print(str1.lower())   
print(str1.title())
print(str1.split(" "))   
print(type(str1))   

#Print the length of String
print(len(str1)) 

#Joining in String
str1 = " ".join(str1)  
print(str1)   


#Count the character of String
print(str1.count('i'))  
print(str1.count("a"))  
print(str1.count('n'))     

#Search the index of String
print(str1.index('i'))   
print(str1.index('n'))     

#Fing the charracter in String
print(str1.find('i'))  
print(str1.find("T"))  
print(str1.find('n'))  
print(str1.find('N')) 
print(str1.find('O'))    
 
#Check the String in String  
str = "There is a lion"  
print("lion" in str)  

str1 = "The best thing in life is free"  
if "free" in str1: 
    print("free is present in String")   

print('expensive' not in str1)  

if 'expensive' not in str1: 
    print("No,'expensive' not present in str1")  

# Combine the String and Integer  
str = "My name is Aanchal and i am {}"  
num = 23 
print(str.format(num))  

myOrder = "I want {} pieces of item {} for {} dollar"  
quantity = 3 
itemno = 567  
price = 49.95  
print(myOrder.format(quantity,itemno,price))  

myOrder = "I want to pay {2} dollar for {0} pieces of item {1}"  
quantity = 3; 
itemno = 567 
price = 49.95  
print(myOrder.format(quantity,itemno,price))   
 
#Return the first character uppercase in String  
txt ="hello, welcome to my world"  
txt = txt.capitalize()  
print(txt)   

#Return the all character lowercase in String  
str = "Hello, I Am A Aanchal"  
str = str.casefold()  
print(str)   

#Return the center align the String  
str = "banana"  
str = str.center(20)    
print(str) 
 
str = "Apple"
str = str.center(20,"O") 
print(str)   

#Returns the encode in the String 
str = "my name is Aanchal"  
str = str.encode()  
print(str)  

#Returns true if the String end with specified value  
str ="Hello , welcome to my world."  
str = str.endswith(".")  
print(str)   

str = "Hello , my name is Aanchal."  
str = str.endswith("is Aanchal.") 
print(str)   

str = "Hello , my name is Aanchal."  
str = str.endswith("is Aanchal.",5,11)  
print(str)  

#Set the tab size to the specified number of whitespaces  
str = "H\te\tl\tl\to"  
str = str.expandtabs(2)  
print(str)   
 
str ="A\ta\tn\tc\th\ta\tl" 
str = str.expandtabs(0) 
print(str)     

str = "S\ti\tn\tg\th"  
str = str.expandtabs(4)  
print(str)

