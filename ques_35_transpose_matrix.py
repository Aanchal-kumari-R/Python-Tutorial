rows = int(input("Enter no. of rows :- ")) #2
cols = int(input("Enter no. of columns:- ")) # 2 

matrix = [] # 1 ,2 / 3,4
for i in range(rows):# 0,1
    matrix.append([]) #1,2/3,4 
    for j in range(cols): #0,0/0,1/1,0/1,1
        matrix[i].append([j]) #0,0/0,1/1,0/1,1,
        print("Value in row: ", i+1,"column :", j+1, ":- " ,end = " ") #1,1= 1 /1,2= 2 /2,1 = 3 /2,2= 4
        matrix[i][j] = int(input()) #1 ,2,3,4


# print("Enter the elements in matrix1 :- ") 
# matrix = [] 

# for i in range(rows):  
#     a = []
#     for j in range(cols):  
#         a.append(int(input())) 
#     matrix.append(a) 

# print("Matrix is:- ") 

# for i in range(rows): 
#     for j in range(cols): 
#         print(matrix[i][j], end = " ") 
#     print() 


print("\n Matrix is :-  \n") 

for m in matrix:  
    print(m) 

trans_matrix = [] # [1,2],  [0,0] 
                  # [3,4]    [0,0]

for i in range(cols): #0,1    
    trans_matrix.append([])#0 ,1
    for j in range(rows):#0,0 /0,1/1,0/1,1
        trans_matrix[i].append([j])#0,0 =0 /0,1 = 0/1,0 = 0/1,1 = 0
        trans_matrix[i][j] = 0 #0,0 =0/ 0,1 = 0 / 1,0 = 0/ 1,1 = 0

print("\n\n Transpose Matrix is :-  \n\n")  

for i in range(rows):# 0,1
    for j in range(cols):#0,0 = 1 / 0,1 = 2 /1,0 = 3/1,1 = 4
        trans_matrix[j][i] = matrix[i][j] #0,0 = 0,0 = 1 /1,0 = 0,1 = 2/ 0,1 = 1,0= 3 /1,1 = 1,1 = 4 

        # [1,3] 
        # [2,4]


for tm in trans_matrix: 
    print(tm)