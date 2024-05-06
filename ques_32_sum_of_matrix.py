# 1st way through user input
row = int(input("Enter the numbers of row :- ")) 
col = int(input("Enter the numbers of col :- ")) 

matrix1 = [] 
print("Enter the elements of matris1:- ") 
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

row1 = int(input("Enter the numbers of rows :- ")) 
col1 = int(input("Enter the numbers of col :-")) 

matrix2 = [] 
print("Enter the elements of Matrix2 :- ") 
for i in range(row1): 
    a = [] 
    for j in range(col1): 
        a.append(int(input())) 
    matrix2.append(a)  

print("Second Matrix is:- ") 
for i in range(row): 
    for j in range(col): 
        print(matrix2[i][j],end = " ") 
    print()  

print("Sum of matrix is:- ")  
matrix = [[0 for i in range(row)] for j in range(col)] 
 
for i in range(row): 
    for j in range(col): 
       matrix[i][j] = matrix1[i][j] + matrix2[i][j]  

for m in matrix: 
    print(m) 

# 2nd way :-  

m1 = [[1,2,3], 
      [2,3,5], 
      [4,5,6]] 

m2 = [[3,4,5], 
      [3,5,6], 
      [4,6,7]] 

matrix = [[0,0,0], 
          [0,0,0], 
          [0,0,0]] 

for i in range(len(m1)): 
    for j in range(len(m1[0])): 
        matrix[i][j] = m1[i][j] + m2[i][j]  

for m in matrix: 
    print(m)

