def arraySum(arr):
    tot = 0
    if len(arr) == 1:
        return arr[0]
    else:
        tot = arr[0] + arraySum(arr[1:])
    return tot


myArr = [2,3,4,5]
print(arraySum(myArr))