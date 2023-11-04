# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

def replaceElements(arr: list[int]) -> list[int]:
    max_so_far = 0
    for i in range(len(arr)-1, -1, -1):
        arr[i], max_so_far = max_so_far, max(max_so_far, arr[i])
    arr[-1] = -1
    return arr


# test
arr = [17,18,5,4,6,1]
print(replaceElements(arr)) # [18,6,6,6,1,-1]

