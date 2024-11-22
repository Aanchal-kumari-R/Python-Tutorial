punc = """~!@#$%^&*()_{}[]:;|>?<|.,'/""" 

string = input('Enter some line of string here:- ') 
empty_str = " " 

for i in string: 
    if i not in punc: 
        empty_str += i 
print(empty_str)