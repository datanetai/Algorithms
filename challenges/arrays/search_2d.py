# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue
            else:
                return search_array(row, target)
        return False

def search_array(arr: list[int], target: int) -> bool:
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return False

matrix =  [[1,3]]

target = 1
print(searchMatrix(matrix, target))