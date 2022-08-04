def binary_search(A, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if x == A[mid]:
        return mid
    elif x < A[mid]:
        return binary_search(A, x, low, mid - 1)
    else:
        return binary_search(A, x, mid + 1, high)

def binary_search(A,x):
    low=A[0]
    high=A[len(A)]
    while low<high:
        mid=(low+high)//2
        if x==A[mid]:
            return mid
        elif x<A[mid]:
            high=mid-1
        else:
            low=mid+1