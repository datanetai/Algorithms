def inversion(A):
    count=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                count+=1
    return count

def merge(A,p,q,r):
    count=0
    mid=q-p+1
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
            count+=mid-i
            if(count>0):
                print("count {0} L {1} R {2} mid {3}".format(count,L,R,mid))
    return count

def mergesort(A,p,r):
    count=0
    if(p<r):
        q=(p+r)//2
        count=mergesort(A,p,q)
        count+=mergesort(A,q+1,r)
        count+=merge(A,p,q,r)
    return count

A=[1,20,6,4,5]
print(mergesort(A,0,4))
print(A)