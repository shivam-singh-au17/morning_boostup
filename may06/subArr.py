
arr = [1, 2, 7]


count = 0
for i in range(0, len(arr)):
    result = []
    for j in range(i, len(arr)):
        result.append(arr[j])
        print(result)
        if 7 in result:
            count = count + 1

print("count ",count)


