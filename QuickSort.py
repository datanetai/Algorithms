import random
def QuickSort(A):
    if len(A)<=1:
        return A
    pivot=random.choice(range(len(A)))
    E=[A[pivot]]
    L,R=partition(A,pivot)
    return QuickSort(L)+E+QuickSort(R)

def partition(A,pivot):
    L=[]
    R=[]
    for i in range(len(A)):
        if i!=pivot:
            if A[i]<A[pivot]:
                L.append(A[i])
            else:
                R.append(A[i])
    return L,R

    
#test QuickSort
A=[1,1,1,1,1,1,12,3,4,4,4,4,4,5,5,62,2,2,2,1,9]
print(QuickSort(A))