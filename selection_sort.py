def findSmallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append((arr.pop(smallest_index)))
    return newArr

myArr = [5,7,2,3,10]
print(selectionSort(myArr))