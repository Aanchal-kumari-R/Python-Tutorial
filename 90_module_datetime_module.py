"""datetime module:- datetime is a module in python not a data type. It handles data and time.  
It has year , month , day , hour , minute , second , microsecond and tzinfo attributes."""

import datetime  

# datetime object :- A datetype object is a single object containing all the information from a date object  
# and a time object. 
#  
x = datetime.datetime.now() 
print(x)  

d = datetime.datetime(2001,2,15) 
print(d)  


"""  
strftime() method:- strftime() method takes one parameter, format ,to specify the format of the returned string.

%b ->  month name , short version           Dec 
%B ->  month name , full version            December
%m ->  month as a number 01-12              12 
%y ->  year, short version without century  18 
%Y -> year, full version                    2018
%H -> hour , 00-12                          09 
%P -> AM/PM                                 PM 
%M -> Minute 00-59                          41
%d -> day of the month 01-31                15 
%S -> Seconds 00-59                         45 
%f -> Microseconds 000000-999999          345678 
""" 

b = datetime.datetime.now() 
now = b.strftime("%y") 
print(now) 