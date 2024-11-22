#maketrans = returns a mapping table that can be used with the translate() method to replace specified characters
txt = "Hello Sam!"   
mytable = txt.maketrans("S","P")  
print(txt.translate(mytable)) 

txt = "Hi Sam!"  
x = "mSa"  
y = "eJo"  
mytable = str.maketrans(x,y)  
print(txt.translate(mytable))   

txt = "Good night Sam!"  
x = "-mSa-"  
y ="-eJo-" 
z = "-odnght-"  
mytable = str.maketrans(x,y,z)  
print(txt.translate(mytable))   

txt = "Good night Sam!"  
x = "mSa"  
y = "eJo"  
z = "odnght"  
print(txt.maketrans(x,y,z)) 
 
#partition() = Searches for a specified string and split the string into a tuple containing three elements  
txt = "I could eat bananas all day"  
x = txt.partition("bananas")  
print(x)     

txt = "I could eat bananas all day"  
x = txt.partition("apples")  
print(x)  

#rfind() = returns the last occurence of the specified value   
txt = "Mi Casa, su case."  
x = txt.rfind("case") 
print(x)  

txt = "Hello, welcome to my world!"  
x = txt.rfind("e")  
print(x) 

txt = "Hello, welcome to my world!"  
x = txt.rfind("e",5,10)  
print(x)  

txt = "Hello, welcome to my world!"    
print(txt.rfind("q"))
txt = "Hello, welcome to my world!"  
print(txt.rfind("q"))
 
#rindex() = returns the last occurence of the specified value  
txt = "Mi Case, su case"  
x = txt.rindex("case")  
print(x)  

#rjust() = returns right align the string using a specified characters  

txt = "banana"  
x = txt.rjust(20) 
print(x)  

txt = "banana" 
x = txt.rjust(20,"O")  
print(x)  

#rpartition() = Searches the last occurence of a specified string and splits the string into a tuple containing three element 
txt = "I could eat bananas all day, bananas my favourite fruit"  
x = txt.rpartition("bananas") 
print(x)  

txt = "I could eat bananas all day, bananas my favourite fruit"  
x = txt.rpartition("apples")  
print(x)  

#rsplit = returns split a string into a list, starting from the right 
txt = "apple, bananas, cherry"  
x = txt.rsplit(",") 
print(x)  

txt = "apple, bananas, cherry"  
x = txt.rsplit(",",1)  
print(x)

#splitlines() = Return a string into a list 
txt = "Thank you for the music\n Welcome to the jugle"  
x = txt.splitlines()  
print(x)   
 
txt = "Thank you for the music\n Welcome to the jugle"  
x = txt.splitlines("True")  
print(x) 

#swapecase() = returns a string where all the upper case letters are lowercase and vice versa 
txt = "Hello My Name Is PETER"  
x = txt.swapcase() 
print(x)    

#translate() = returns a string where some specified characters are replaced 
mydict = {83:80}  
txt = "Hello Sam!"  
print(txt.translate(mydict))  

#zfill() = adds zero at the beginning of the string  
txt = "50"  
x = txt.zfill(10) 
print(x) 

a = "hello" 
b = "welcome to the jungle" 
c = "10.00"  
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))











