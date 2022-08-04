def mergesort(A):
    if(len(A)==1):
        return A
    n=len(A)
    L=mergesort(A[:n//2])
    R=mergesort(A[n//2:])
    return merge(L,R)

def merge(L,R):
    i,j=0,0
    n=len(L)+len(R)
    result=[]
    while i<len(L) and j<len(R):
        if(L[i]<R[j]):
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j=j+1
    while i<len(L):
        result.append(L[i])
        i+=1
    while j<len(R):
        result.append(R[j])
        j+=1
    return result

def merge(A,p,q,r):
    #using pointer
    L=A[p:q+1]
    R=A[q+1:r+1]
    # print(len(L),len(R))
    # print(r-p)
    L.append(float('inf'))
    R.append(float('inf'))
    i,j=0,0
    for k in range(p,r+1):
        if(L[i]<=R[j]):
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

def mergesort(A,p,r):
    if(p<r):
        q=(p+r)//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
#test mergesort
A=[7,8,9,10,1,2,3,4,5,6]
print(mergesort(A,0,len(A)-1))
print(A)