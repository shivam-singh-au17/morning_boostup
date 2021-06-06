
arr = [1, 2, 3, 4, 5]


def oddFinder(arr):

    for i in range(0, len(arr)):
        count = 0
        result = []

        for j in range(i, len(arr)):
            result.append(arr[j])

            for k in range(0, len(result)):
                if result[k] % 2 == 1 and result[len(result) - 1] % 2 == 1:
                    count = count + 1
        return count 

     
print(oddFinder(arr))



def func(n):
    flag = False
    for i in range(0, len(n)):
        if n[i] % 2 == 0:
            flag = True
    
    if flag == True:
        return "yes"
    else:
        return "no"

print(func([1,2,3,5,7,9]))