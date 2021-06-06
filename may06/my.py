
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


row = len(mat)
col = len(mat[0])

# x = 1
# for i   in range(0, row):
#     print(mat[x-1][i])
#     print(mat[i][x-1])


# for i in range(0, row):
#     for j in range(0, col):
#         if i == j:
#             print(mat[i][j])


for i in range(0, row):
    for j in range(0, col):
        if (i == row - j - 1):
            print(mat[i][j])

            