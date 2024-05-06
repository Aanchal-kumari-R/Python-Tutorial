row = int(input("Enter the row number:")) 
col = int(input("Enter the col number:")) 

matrix = [] 
print("Enter the elements for matrix:")
for i in range(row): 
    a = [] 
    for j in range(col): 
        a.append(int(input())) 
    matrix.append(a)   

print("Matrix is:-")
for i in range(row): 
    for j in range(col): 
        print(matrix[i][j],end = " ") 
    print()    

