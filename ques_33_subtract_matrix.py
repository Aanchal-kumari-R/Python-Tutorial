row = int(input("Enter the number of row :- ")) 
col = int(input("Enter the number of column :- ")) 

print("Enter the elements in the matrix1 :- ") 
matrix1 = [] 
for i in range(row): 
    a = [] 
    for j in range(col): 
        a.append(int(input())) 
    matrix1.append(a) 

print("First Matrix is:- ") 
for i in range(row): 
    for j in range(col): 
        print(matrix1[i][j], end = " ") 
    print() 

row = int(input("Enter the number of row :- ")) 
col = int(input("Enter the number of col :- ")) 

print("Enter the elements in the matrix2 :-") 
matrix2 = [] 
for i in range(row): 
    a = [] 
    for j in range(col): 
        a.append(int(input())) 
    matrix2.append(a) 

print("Second Matrix is:- ") 
for i in range(row):  
    for j in range(col): 
        print(matrix2[i][j], end = " ") 
    print()  

print("Subtraction of matrix is:- ")
result = [[0 for i in range(row)]for j in range(col)]  
for i in range(row): 
    for j in range(col): 
        result[i][j] = matrix1[i][j] - matrix2[i][j]   

for r in result:
       print(r)

