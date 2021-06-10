



mat = [
    [1, 2, 3, 1],
    [4, 5, 6, 4],
    [7, 8, 9, 7],
    [3, 6, 9, 5]
]

row = len(mat)
col = len(mat[0])

for r in range(0, row):
    if r % 2 == 0:
        for c in range(col -1, -1 ,-1):
            print(mat[r][c], end=" ")
    else:
        for c in range(0, col):
            print(mat[r][c], end=" ")
    print()




# for c in range(0, row):
#     for r in range(col - 1, -1, -1):
#         print(mat[r][c], end=" ")
#     print()


# for c in range(col - 1, -1, -1):
#     for r in range(0, row):
#         print(mat[r][c], end=" ")
#     print()


