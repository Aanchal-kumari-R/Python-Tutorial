"Math Module:- It a module that contains some method that perform some task related to numeric value."
import math 

# ceil() method :- The ceil method rounds a number UP to the nearest integer, if neccessary, and return the result.   
x  = 10.5   
y = 11
print(math.ceil(x))
print(math.ceil(y)) 

# fabs() method :- The method returns the absolute value of the given value. 

# a = -11 
a = +10 
print(math.fabs(a))  

# factorial() method :- factorial method returns the factorial of a given number.

f = 5 
print(math.factorial(f)) 

# floor() method :- The floor method rounds a number Down to the nearest integer, if neccessary, and return the result.
f1 = 10.5 
print(math.floor(f1)) 

# fsum() method :- Return an accurate floating point sum of values in the iterable. 
l = [10,20,30,40] 
print(math.fsum(l)) 

# sqrt() method :- Return the square root of given number.

s = 9 
print(math.sqrt(s))  

# pi :- This method return the constant value of pi. 
p = math.pi 
print(p)