# def bubble_sort(A):
      #sorting from start
#     for i in range(len(A)):
#         for j in range(len(A)-1, i, -1):
#             if (A[j]<A[j-1]):
#                 A[j],A[j-1]=A[j-1],A[j]
#         print(A)
#     return A

def bubble_sort(A):
    #sorting from end
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if (A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]
        print(A)
    return A
#test bubble_sort

print(bubble_sort([3,2,2,1,5,7,4,2,1,0]))