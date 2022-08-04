import random
def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def randomized_partition(A,p,r):
    #for aver
    i = random.randint(p,r)
    A[i],A[r] = A[r],A[i]
    return partition(A,p,r)
def tail_recursive_quicksort(A,p,r):
    while p < r:
        q = hoare_partition(A,p,r)
        tail_recursive_quicksort(A,p,q-1)
        p = q+1

def hoare_partition(A,p,r):
    x = A[p]
    i = p-1
    j = r+1
    while True:
        #i j value
        print("i = {}, j = {} at start of loop".format(i,j))
        j -= 1
        while A[j] > x:
            j -= 1
        i += 1
        while A[i] < x:
            i += 1
        print("i = {}, j = {} at end of loop".format(i,j))
        if i < j:
            A[i],A[j] = A[j],A[i]
        else:
            return j
A=[4,6,3,2,1,5]
tail_recursive_quicksort(A,0,len(A)-1)
print(A)
#visulize hoare partition function using heartrate

