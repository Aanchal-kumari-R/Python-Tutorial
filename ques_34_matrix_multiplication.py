matrix1_of_row = int(input("Enter the number of rows :- ")) 
matrix1_of_col = int(input("Enter the number of column :- ")) 

print("Enter the elements in matrix1 :- ") 
matrix1 = [] 

for i in range(matrix1_of_row):  
    a = []
    for j in range(matrix1_of_col):  
        a.append(int(input())) 
    matrix1.append(a) 

print("Matrix1 is:- ") 

for i in range(matrix1_of_row): 
    for j in range(matrix1_of_col): 
        print(matrix1[i][j], end = " ") 
    print() 


matrix2_of_row = int(input("Enter the number of rows :- ")) 
matrix2_of_col = int(input("Enter the number of column :- ")) 

print("Enter the elements in matrix2 :- ") 
matrix2 = [] 

for i in range(matrix2_of_row):  
    a = []
    for j in range(matrix2_of_col):  
        a.append(int(input())) 
    matrix2.append(a) 

print("Matrix2 is:- ") 

for i in range(matrix2_of_row): 
    for j in range(matrix2_of_col): 
        print(matrix2[i][j], end = " ") 
    print() 
     
print("Multiplication of matrix is:- ")

result = [[0 for j in range(matrix2_of_col)] for i in range(matrix1_of_row)] 
for i in range(len(matrix1)): 
    for j in range(len(matrix2[0])): 
        for k in range(len(matrix2)): 
            result[i][j] += matrix1[i][k] * matrix2[k][j] 
print()  

for i in result: 
    print(i)