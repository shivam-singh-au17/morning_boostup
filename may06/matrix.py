
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


mat2 = [
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
]

# newMat = mat + mat2
# print(newMat)


# i <= j

# print(mat[0][0])
# print(mat[0][1])
# print(mat[0][2])


row = len(mat)
col = len(mat[0])

# print("row length",row)
# print("col length",col)


# fix_col = 2
# fix_row = 3

# for i in range (0, row):
    # print(mat[i][fix_col - 1])
    # print(mat[fix_row - 1][i], end=" ")



# for i in range(0, row):
#     for j in range(0, col):
#         if i == j:
#             print("daigno",mat[i][j], end= " ")


# for i in range(0, row):
#     for j in range(0, col):
#         if i == row - j - 1:
#             print(mat[i][j])



# sum = 0
# for i in range(0, row):
#     for j in range(0, col):
#         if i <= j:
#             print(mat[i][j])
#             sum += mat[i][j]
# print(sum)



# print()


# sum = 0
# for i in range(0, row):
#     for j in range(0, col):
#         if i >= j:
#             print(mat[i][j])
#             sum += mat[i][j]
# print(sum)



# outerMat = []
# for i in range(0, row - 1):
#     inerMat = []
#     for j in range(0, col - 1):
#         inerMat.append(mat[i][j])
    
#     outerMat.append(inerMat)
      
# print(outerMat)




# outerMat = []
# for i in range(1, row):
#     inerMat = []
#     for j in range(1, col):
#         inerMat.append(mat[i][j])
    
#     outerMat.append(inerMat)
      
# print(outerMat)



outerMat = []
for i in range(0, row):
    inerMat = []
    for j in range(0, col):
        inerMat.append(mat[i][j] + mat2[i][j])
    
    outerMat.append(inerMat)
      
print(outerMat)



print(abs(10 - 20))
        
