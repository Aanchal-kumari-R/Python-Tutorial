#Poisitional Arguments
def groceries(item,price): 
    print("item =", item, " Price =" ,price) 
groceries("Sugar",60)   
groceries(45,"Sugar")

#Keyword Arguments 
groceries(item = "Bread", price=55) 
groceries(price = 65, item="Chocolate")  

#Default Arguments 
def grocery(item, price = 20): 
    print("item = ",item, "price = ",price) 
grocery(item="Bread", price=60) 
grocery("Rice") 
grocery("Milk",44) 
grocery(item = "Milk")   

#Variable Length Arguments  
def calc(*num):  
    add = 0 
    for i in num: 
      add += i  
    print('Addition =',add) 
calc(22,67,78,55) 

#keyword Variable Length Arguments   

# def grocery(**calc): 
#     print("********* Welcome to Sanjiv Grocery Store *********") 
#     price = 0 
#     c= 1 
#     for i,j in calc.items(): 
#         print(f"\t{c}.{i}--{j}") 
#         price+=j   
#         c+=1
#     print("--------------------------------")
#     print("Total Payable Amount = ",price,"Thanks for visiting.") 
# grocery(Bread = 55,Sugar = 56 ,Milk = 45 )   

# def blinkit(*item):
#   df = {'Rice':56, 'Bread':25 ,'Milk' : 28,'Soap': 35}
#   price = 0
#   c=1
#   print("***** Welcome to Sanjiv Grocery Store ********\n")
#   for i in item:
#     print(f"{c}. {i} -- {df[i]}₹ GST - 18%  {df[i]+(df[i]*0.18)}₹")
#     price +=df[i]+(df[i]*0.18)
#     c+=1
#   print("-----------------------------\nTotal Payable Ammount =",price, "\nThanks for Vistings 🤓" )
# blinkit('Bread','Milk','Soap')