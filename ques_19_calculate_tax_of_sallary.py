sallary = eval(input("Enter the sallary to calculate the tax :- " ))  
if sallary<10000: 
    print(sallary, "No tax.") 
elif sallary>10000 and sallary<100000:  
    tax = sallary*0.10
    print(sallary ,"The tax is :",tax)  
elif sallary>100000 and sallary <=200000: 
    tax = sallary*0.20 
    print(sallary, "The tax is :",tax) 