"""
Build a function that has an input as follows and
Inpurt array of distinct numbers and and target sum.The array must be checked for two pairs summed together to give the result of the target and the result must be a the target number

Example
INPUT
array = [3,5,-4,8,11,1,-1,6]
target = 10

OUTPUT
[-1,11]

Space and time complexity are O(n)

"""

# def arr(array,target):
#     for i in array:
#         for v in array:
#             if i + v == target:
#                 print([i,v])
#                 break
#
#
# array1 = [3,5,-4,8,11,1,-1,6]
# target1 = 10
# arr(array1, target1)

##Hash Table O(n^2) T | O(1) Space
def twoNumbertwofor(array, targetNumb):
    for i in range(len(array)-1):
        firstNumber = array[i]
        for j in range(i+1, len(array)):
            secondNumber = array[j]
            if firstNumber+secondNumber == targetNumb:
                return [firstNumber, secondNumber]
    return []


##Hash Table O(n) ST
def twoNumberHash(array, targetNumb):
    nums = {}
    for num in array:
        potentialmatch = targetNumb - num
        if potentialmatch in nums:
            return [potentialmatch, num]
        else:
            nums[num]= True
    return []

def twoNumberSort(array, targetNumb):
    array.sort()
    left = 0
    right = len(array) -1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetNumb:
            return[array[left], array[right]]
        elif currentSum < targetNumb:
            left+=1
        elif currentSum > targetNumb:
            right-=1
    return []

array1 = [3,5,-4,8,11,1,-1,6]
target1 = 10
print(twoNumbertwofor(array1, target1))
print(twoNumberHash(array1, target1))
print(twoNumberSort(array1, target1))
