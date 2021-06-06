

# 1

N = 5
for i in range(1, N + 1):
    res = "";
    for j in range(1, i+1):
        res += "*" + " "
    
    print(res)
    



print()


# 2

N = 5
for i in range(1, N + 1):
    res = ""
    for j in range(1, N + 1):
        if (i == 1 or i == N or j == N):
            res += "*" + " "
        else:
            res += "  "
        
    
    print(res)
    




print()


# 3

N = 5
for i in range(1, N + 1):
    res = "";
    for j in range(1, N + 1):
        if (i == N or j == N):
            res += "* "
        else:
            res += "  "
        
    
    print(res)
   



# 4

N = 5

for i in range(1, N + 1):
    result = "";
    for j in range(1, N + 1 - i):
        result += " "
    for k in range(1, i + 1):
        result += "*" + " "
    print(result)


# print()


# 5

N = 5

for i in range(1, N + 1):
    result = "";
    for j in range(1, N + 1 - i):
        result += " "
    for k in range(1, i + 1):
        result += "*" + " "
    print(result)
