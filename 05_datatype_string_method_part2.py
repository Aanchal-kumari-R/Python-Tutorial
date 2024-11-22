#Returns true if String is  the combination of alphabets and number  
str ="company12"  
str = str.isalnum()  
print(str)  

str = "company 12"  
str = str.isalnum()  
print(str)   

#Returns true if String is the only combination of character  
str = "companyX"  
str = str.isalpha()  
print(str)   

str ="company12"  
str = str.isalpha()  
print(str)   

#Return true if all characters are ascii character   
str = "company123"  
str = str.isascii() 
print(str)  

#Return true if all characters are decimal  
Str = "1234" 
x = Str.isdecimal() 
print(x)   

a = "\u0030"  
b ="\u0047"  
print(a.isdecimal()) 
print(b.isdecimal())  
  
#Return true if all characters are digit 

str = "23434" 
x = str.isdigit()  
print(x)  

a="\u0030"  
b="\u00B2"  

print(a.isdigit())  
print(a.isdecimal())  

#isidentifire == Returns true if the string is a valid identifire  

txt = "Demo" 
x = txt.isidentifier()  
print(x)   
 
a = "Myfolder"  
b ="Demo002" 
c ="2bring"  
d = "my demo"  

print(a.isidentifier()) 
print(b.isidentifier()) 
print(c.isidentifier()) 
print(d.isidentifier())    

#islower = Returns true if all the characters are in lower case    
str ="hello world"  
x = str.islower() 
print(x)   

a = "Hello world!"  
b = "hello 123"  
c= "mynameisPeter"   

print(a.islower())  
print(b.islower()) 
print(c.islower)
  
#isnumeric = Returns true if all characters are numeric  

str = "332323"  
x = str.isnumeric() 
print(x)  

a="\u0030"  
b="\u00B2"  
c ="10km2"  
d ="-1"  
e = "1.5"  

print(a.isnumeric()) 
print(b.isnumeric())
print(c.isnumeric()) 
print(d.isnumeric())
print(e.isnumeric())   

#isprintable = Returns true if all characters are true  

txt = "Hello!How Are you #1 ?"  
x = txt.isprintable() 
print(x)  

txt = "Hello!\n Are you #1 ?"  
x = txt.isprintable()  
print(x)  

#Return true if all characaters in String are whitespaces  
str = "   "  
x = str.isspace()  
print(x)   

str = "    s    "  
s = str.isspace() 
print(s)  

#istitle = Returs true if  first character in a string are upper case  
str = "Hello World!"  
s = str.istitle() 
print(s)  
 
a = "HELLO, AND WELCOME TO MY WORLD" 
b = "Hello"  
c = "22S Names" 
d = "This Is % ! ?"  

print(a.istitle()) 
print(a.istitle()) 
print(a.istitle())
print(a.istitle())  

#issuper = Returns true if all character are uppercase in a string    
a = "Hello World!" 
b = "hello 123" 
c = "MY NAME IS PETER"  

print(a.isupper()) 
print(b.isupper()) 
print(c.isupper())    

#ljust = returns left align the string using a specified character s  
str = "banana"  
str = str.ljust(20) 
print(str)   

str = "banana" 
str = str.ljust(20,"0")  
print(str)  

