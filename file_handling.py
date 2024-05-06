df1 = open("info.txt","w") 
df1.write("Hello i am aanchal, and i have completed Bca from ignou in 2023.") 
df1.close() 

df2 = open("info.txt","r") 
print(df2.read()) 
df2.close()  

df3 = open("info.txt","a") 
df3.write(" Now i am looking for a new job in Ai.") 
df3.close() 

df2 = open("info.txt") 
print(df2.read()) 
df2.close()   

df3 = open("info.txt","a") 
df3.write(input("Enter more about yourself.")) 
df3.close()  

df2 = open("info.txt") 
print(df2.read()) 
df2.close()     

df3 = open("info.txt","r+")  
print(df3.read())
df3.write(input("Enter something more about yourself.")) 
df3.close()    

df3 = open("my_doc.txt","w+") 
df3.write(input("Enter something more about yourself."))    
print(df3.read())
df3.close()



