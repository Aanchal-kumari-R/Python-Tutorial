# with statement is used for take the place of close() function.
with open("docs.txt","w") as df: 
    df.write("Hello , i am aanchal.") 


# seek():- its return the current position of file. 
# tell():- through thik we can change the position of the file.
with open("docs.txt") as df1: 
    print(df1.read())   
    print(df1.tell())  
    df1.seek(5) 
    print(df1.tell())  

with open("my_doc.txt","w+")  as df:
  df.write(input("Enter something more about yourself."))  
  df.seek(7) 
  print(df.read()) 


# with open("my_doc.txt","r+")  as df: 
#    print(df.read(8))

with open("my_doc.txt","r+")  as df: 
    print(df.read()) 
    df.seek(6) 
    df.write(" Goldi ") 

with open("my_doc.txt","r+")  as df: 
    print(df.read()) 

df = open("intro.txt","w+") 
print("Enter more about yourself.") 
while str != "@": 
    str = input() 
    if str != "@": 
        df.write(str) 
df.seek(0) 
print(df.read()) 
df.close()    

# Binary files  

df1 = open("box6_image.jpg","rb") 
print(df1.read()) 
df1.close() 

df1 = open("box6_image.jpg","rb") 
n1 = df1.read() 
df2 = open("new.jpg","wb") 
df2.write(n1) 

df1.close() 
df2.close()  


df1 = open("myfile.txt","x") 
df1 = open("myfile.txt","w")  
df1.close()