def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2

def max_heapify(A,i, heap_size):
    l=left(i)
    r=right(i)
    if(l<heap_size and A[l]>A[i]):
        largest=l
    else:
        largest=i
    if(r<heap_size and A[r]>A[largest]):
        largest=r

    if largest!=i:
        temp=A[i]
        A[i]=A[largest]
        A[largest]=temp
        max_heapify(A,largest, heap_size)

def min_heapify(A,i, heap_size):
    l=left(i)
    r=right(i)
    if(l<heap_size and A[l]<A[i]):
        smallest=l
    else:
        smallest=i
    if(r<heap_size and A[r]<A[smallest]):
        smallest=r
    if(smallest!=i):
        temp=A[i]
        A[i]=A[smallest]
        A[smallest]=temp
        min_heapify(A,smallest, heap_size)

def build_min_heap(A):
    for i in range(len(A)//2,-1,-1):
        min_heapify(A,i,len(A))

def build_heap(A):
    for i in range(len(A)//2+1,-1,-1):
        max_heapify(A,i, len(A))

def heap_sort(A):
    heap_size=len(A)
    for i in range(len(A)-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heap_size-=1
        max_heapify(A,0, heap_size)
        print(A)
#proriety queue 
def heap_maximum(A):
    return A[0]
def heap_Extract_Max(A):
    if(len(A)==0):
        return "heap underflow"
    max=A[0]
    A[0]=A[-1]
    A.pop()
    heap_size-=1
    max_heapify(A,0,len(A))
    return max

def heap_extract_min(A):
    if(len(A)==0):
        return "heap underflow"
    heap_size=len(A)
    min=A[0]
    A[0]=A[-1]
    A.pop()
    heap_size-=1
    min_heapify(A,0,len(A))
    return min

def heap_increase_key(A,i,key):
    if key<A[i]:
        return "new key is smaller than current key"
    A[i]=key
    while i>0 and A[parent(i)]<A[i]:
        A[i],A[parent(i)]=A[parent(i)],A[i]
        i=parent(i)
    
def max_heap_insert(A,key):
    heap_size+=1
    A.append(0)
    heap_increase_key(A,len(A)-1,key)


A=[15,4,2,24,5,7,8,6,5,3,3,2]
heap_size=len(A)
build_heap(A)
print(A)
# heap_sort(A)
# print(A) 

def merge_sorted_list(lists):
    n=len(lists)
    lowest=[]
    for i in range(n):
        lowest.append(lists[i][0])
    heap_size=len(lowest)
    build_heap(lowest)
    print(lowest)
    result=[]
    while heap_size>0:
        result.append(heap_extract_min(lowest))
        if len(lists[lowest.index(result[-1])])>1:
            heap_size+=1
            lowest.append(lists[lowest.index(result[-1])][1])
            heap_increase_key(lowest,heap_size-1,lists[lowest.index(result[-1])][1])
            lists[lowest.index(result[-1])].pop(0)
            
        else:
            heap_size-=1
    return result

lists=[[1,2,3],[4,5,6],[7,8,9]]
print(merge_sorted_list(lists))

