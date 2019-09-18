def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def findLargest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index

def selectionSort_S(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def selectionSort_L(arr):
    newArr = []
    for i in range(len(arr)):
        largest = findLargest(arr)
        newArr.append(arr.pop(largest))
    return newArr

print(selectionSort_S([5,3,6,2,10]))
print(selectionSort_L([5,3,6,2,10]))
