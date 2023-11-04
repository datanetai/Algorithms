def hash(k,j):
    return (k+j) % 10


def hash_insert(T,k):
    m=10
    j=0

    while j!=m:
        i = hash(k,j)

        if T[i]==None or T[i]=="DELETED":
            T[i]=k
            return
        j+=1
    raise OverflowError("Hash table overflow")

def hash_search(T,k):
    m=10
    j=0

    while j!=m or T[i]!=None:
        i = hash(k,j)

        if T[i]==k:
            return i
        j+=1
    raise None

def hash_delete(T,k):
    i = hash_search(T,k)
    T[i]="DELETED"


T=[None]*10
L=[1,222,66,33,7,89,9,9]
for i in L:
    hash_insert(T,i)

print(T)
print(hash_search(T,1))

