def insertion_sort(A):
    for i in range(1,len(A)):
        cur=A[i]
        j=i-1
        while A[j]>cur and j>=0:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=cur
    return A

#test insertion_sort
A=[1,3,5,2,4,6]
print(insertion_sort(A))